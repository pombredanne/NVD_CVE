# NVD_CVE
Build CVE data model using the the NVD JSON feeds.

This implementation of the NVD JSON feeds incorporates the following - 

1. Load all the JSON feeds and combine them as 1 single JSON to be ingested in Postgres Database.
2. Connect DJANGO ORM with Postgres Database.
3. Create a data model from the given JSON schema (https://csrc.nist.gov/schema/nvd/feed/1.1/nvd_cve_feed_json_1.1.schema) with addtional external schema given in the reference.
4. Create Django ORM queries to filter information based on the requirements.
5. Finally, gives a solution to any query posed by the data model.
