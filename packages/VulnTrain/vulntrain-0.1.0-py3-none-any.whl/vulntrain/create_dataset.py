"""
    Creates a text/description dataset using vulnerabilities description from Vulnerability-Lookup.

    Author: Cédric Bonhomme / CIRCL

"""
import json
from typing import Any, Generator

import valkey
from datasets import Dataset, DatasetDict


class VulnExtractor:
    def __init__(self):
        self.valkey_client = valkey.Valkey(
            host="127.0.0.1",
            port=10002,
            decode_responses=True,
        )


    def get_vulnerability_meta(self, vulnerability_id: str) -> dict[str, str | dict[str, Any]]:
        _vid = vulnerability_id.lower()
        to_return: dict[str, str | dict[str, Any]] = {}
        for meta_name, meta_uuid in self.valkey_client.hgetall(f'{_vid}:meta').items():
            if self.valkey_client.exists(f'{meta_name}:{meta_uuid}'):
                if self.valkey_client.type(f'{meta_name}:{meta_uuid}') == 'string':  # type: ignore[no-untyped-call]  # noqa
                    if _meta_str := self.valkey_client.get(f'{meta_name}:{meta_uuid}'):
                        to_return[meta_name] = _meta_str
                elif self.valkey_client.type(f'{meta_name}:{meta_uuid}') == 'hash':  # type: ignore[no-untyped-call]  # noqa
                    if _meta_hash := self.valkey_client.hgetall(f'{meta_name}:{meta_uuid}'):
                        to_return[meta_name] = _meta_hash
            else:
                print(f'Unable to find meta {meta_uuid} for {meta_name}')
        return to_return


    def get_vulnerability(self, vulnerability_id: str,
                          *, with_meta: bool | None=False) -> dict[str, Any] | None:
        _vid = vulnerability_id.lower()
        _vuln = self.valkey_client.get(_vid)
        if not _vuln:
            return None
        vuln = json.loads(_vuln)
        if with_meta:
            if meta := self.get_vulnerability_meta(_vid):
                vuln['vulnerability-lookup:meta'] = meta
        return vuln

    def get_all(self, source: str = "", /, with_meta: bool=False) -> Generator[dict[str, Any], None, None]:
        """This method will scan a complete source and yield the vulnerabilities.
        It is up to the caller to handle the yielded entries as it will be a lot"""
        if source:
            key = f'index:{source}'
        else:
            key = 'index'
        for vuln_id, _ in self.valkey_client.zscan_iter(key):
            if vuln := self.get_vulnerability(vuln_id, with_meta=with_meta):
                yield vuln
    
    def __call__(self):
        count = 0
        for vuln in self.get_all("nvd", True):
            count += 1
            if count == 10000:
                return

            vuln_cpes = []
            if vulnrichment := vuln["vulnerability-lookup:meta"].get("vulnrichment", False):
                containers = json.loads(vulnrichment["containers"])
    
                # Check ADP section
                if "adp" in containers:
                    for entry in containers["adp"]:
                        if "affected" in entry:
                            for affected in entry["affected"]:
                                if "cpes" in affected:
                                    vuln_cpes.extend(affected["cpes"])
                
                # Check CNA section
                if "cna" in containers and "affected" in containers["cna"]:
                    for affected in containers["cna"]["affected"]:
                        if "cpes" in affected:
                            vuln_cpes.extend(affected["cpes"])

                # for elem in vulnrichment["containers"]["adp"]["affected"]:
                #     if "cpes" in elem:
                #         print(elem)
                #         vuln_cpes = elem["cpes"]
                #         break
                #     else:
                #         vuln_cpes = []

            vuln_id = vuln["cveMetadata"]["cveId"]

            vuln_title = vuln["containers"]["cna"].get("title", "")

            for description in vuln["containers"]["cna"].get("descriptions", []):
                if description["lang"].lower() in ["en", "en-sn", "en-us"]:
                    vuln_description = description["value"]
                    break
            else:
                continue

            # if not vuln_cpes:
            #     for elem in vuln["containers"]["cna"]["affected"]:
            #         if "cpes" in elem:
            #             vuln_cpes = elem["cpes"]
            #             break
            #     else:
            #         vuln_cpes = []



            # print(vuln_cpes)

            vuln_data = {
                "id": vuln_id,
                "title": vuln_title,
                "description": vuln_description,
                "cpes": vuln_cpes,
            }
            yield vuln_data





def main():
    extractor = VulnExtractor()

    vulns = list(extractor())

    def gen():
        for vuln in vulns:
            yield vuln

    dataset = Dataset.from_generator(gen)
    train_test_split = dataset.train_test_split(test_size=0.1)
    dataset_dict = DatasetDict(
        {"train": train_test_split["train"], "test": train_test_split["test"]}
    )

    print(dataset_dict)
    # dataset_dict.push_to_hub("cedricbonhomme/vulnerability-descriptions")
    dataset_dict.push_to_hub("circl/vulnerability-dataset")


if __name__ == "__main__":
    main()
