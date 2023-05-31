# OpenAPI Generator Action

![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/hatamiarash7/openapi-generator?color=%2300baba&label=Marketplace&logo=github)

This GitHub Action allows you to automatically generate code using the OpenAPI Tools generator. The OpenAPI Tools generator provides a set of powerful features to generate client SDKs, server stubs, documentation, and more from your OpenAPI specification file.

## Usage

Here's an example workflow that demonstrates how to use this GitHub Action:

```yaml
name: Generate Code from OpenAPI

on:
  release:
    types: [published]

jobs:
  generate_code:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Generate code
        uses: hatamiarash7/openapi-generator@v0.1.0
        with:
          generator: python
          openapi-file: example.yml

      # Do anything you want with the generated code
      - name: Do anything
        run: ...
```

## Inputs

| Name            | Type     | Default          | Description                                                                         |
| --------------- | -------- | ---------------- | ----------------------------------------------------------------------------------- |
| `generator`     | Required |                  | The name of the generator to use e.g. "typescript-angular"                          |
| `generator-tag` |          | `latest`         | The Docker tag of the `openapitools/openapi-generator-cli` image to use             |
| `openapi-file`  |          | `./openapi.json` | The path to the OpenAPI document                                                    |
| `openapi-url`   |          | `UNSET`          | If set, the OpenAPI document will be loaded from this URL instead of `openapi-file` |
| `config-file`   |          | `UNSET`          | The path to the config file to be passed along to the generator                     |
| `template-dir`  |          | `UNSET`          | The path to the folder containing the template files                                |
| `command-args`  |          |                  | Additional arguments to pass through to the generator                               |

---

## Support

[![Donate with Bitcoin](https://en.cryptobadges.io/badge/micro/3GhT2ABRuHuXGNzP6DH5KvLZRTXCBKkx2y)](https://en.cryptobadges.io/donate/3GhT2ABRuHuXGNzP6DH5KvLZRTXCBKkx2y) [![Donate with Ethereum](https://en.cryptobadges.io/badge/micro/0x4832fd8e2cfade141dc4873cc00cf77de604edde)](https://en.cryptobadges.io/donate/0x4832fd8e2cfade141dc4873cc00cf77de604edde)

[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/D1D1WGU9)

<div><a href="https://payping.ir/@hatamiarash7"><img src="https://cdn.payping.ir/statics/Payping-logo/Trust/blue.svg" height="128" width="128"></a></div>

## Contributing

Don't be shy and reach out to us if you want to contribute.

1. Fork it !
2. Create your feature branch : `git checkout -b my-new-feature`
3. Commit your changes : `git commit -am 'Add some feature'`
4. Push to the branch : `git push origin my-new-feature`
5. Submit a pull request

## Issues

Each project may have many problems. Contributing to the better development of this project by reporting them.
