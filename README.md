## Welcome to Canvas Medical's open source SDK

This repository is meant to support developers who are customizing their Canvas environments using the [canvas-workflow-kit](https://docs.canvasmedical.com/docs/sdk-quickstart).

This open source project is new, and we will be updating this documentation as we grow.
For now, this is where developers can find examples of different [protocols](https://docs.canvasmedical.com/docs/canvas-cli#upload) that can be uploaded to Canvas environments to support clinical workflows. These protocols are calculated on specified [events](https://docs.canvasmedical.com/docs/event-types) emitted from the canvas platform (you can choose whatever event you want to listen for).

Here are examples of different protocols you can find in this repo:

- On appointment creation, create a task to remind that patient of their upcoming appointment.
- On appointment update or creation, send a notification to an external server with relevant information about the appointment.
- On patient data change, show a protocol in each patient's chart with useful patient links for the clinical user.

We encourage developers to fork this repo and share their custom protocol. The canvas-workflow-kit gives developers the flexibility to implement a variety of custom workflows; imagine what we could do if we shared them all!

## Getting Started

At Canvas Medical, we use [Poetry](https://python-poetry.org/) for packaging and dependency management.

Fork this repo & `git clone git@github.com:canvas-medical/open-source-sdk.git`

from the `open-source-sdk` directory run

```
poetry install
```

This will also install `canvas-workflow-kit`. Please follow the configuration instructions found in the [documentation](https://docs.canvasmedical.com/docs/canvas-cli#settings).

The protocol examples found in `open-source-sdks/canvas_workflow_helpers/protocols` can all be uploaded to your canvas instance by running

```
canvas-cli upload FILENAME
```

We hope these examples can provide more insight into building your protocols.

## Contributing

Please review our [Contributing Guidelines](https://github.com/canvas-medical/open-source-sdk/blob/main/CONTRIBUTING.md) and [Code of Conduct](https://github.com/canvas-medical/open-source-sdk/blob/main/CODE_OF_CONDUCT.md) before contributing to this open source repo.
