stripe-sql
==========
[![No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech)
[![License](https://img.shields.io/badge/license-Apache--2.0%20OR%20MIT%20OR%20CC0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort)

Stripe API SQLalchemy models.

## Development guide

None of the JSON-ref dereferencing tools I Google'd actually worked. So I wrote this script with `jq` and `bash` to generate all the JSON schema files you find in this repository:

```sh
$ ./scripts/get_stripe_openapi_gen_json_schema.bash
```

(it downloads from https://github.com/stripe/openapi)

Now you can use the regular [cdd-python](https://github.com/offscale/cdd-python) (`pip install python-cdd`) CLI to generate SQLalchemy from these JSON-schema files:
```sh
$ for json_file in 'json_schemas'/*.json; do
     python -m cdd gen --emit-and-infer-imports \
                       --name-tpl '{name}' \
                       --input-mapping "$json_file" \
                       --parse 'json_schema' \
                       --emit 'sqlalchemy' \
                       --output-filename 'stripe_openapi/'"${json_file//+(*\/|.*)}"'.py'
  done
```

---

## License

Licensed under any of:

- Apache License, Version 2.0 ([LICENSE-APACHE](LICENSE-APACHE) or <https://www.apache.org/licenses/LICENSE-2.0>)
- MIT license ([LICENSE-MIT](LICENSE-MIT) or <https://opensource.org/licenses/MIT>)
- CC0 license ([LICENSE-CC0](LICENSE-CC0) or <https://creativecommons.org/publicdomain/zero/1.0/legalcode>)

at your option.

### Contribution

Unless you explicitly state otherwise, any contribution intentionally submitted
for inclusion in the work by you, as defined in the Apache-2.0 license, shall be
licensed as above, without any additional terms or conditions.
