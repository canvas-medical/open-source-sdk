## Welcome to Canvas Medical's open source SDK

This repository is meant to support developers who are customizing their Canvas environments using the [canvas-workflow-kit](https://docs.canvasmedical.com/docs/sdk-quickstart). Installing the dependencies in this repo will also install `canvas-workflow-kit`.

This open source project is new, and we will be updating this documentation as we grow. :bug::butterfly:

For now, this is where developers can find the following:

### Protocols

[`canvas_workflow_helpers/protocols`](https://github.com/canvas-medical/open-source-sdk/tree/main/canvas_workflow_helpers/protocols) contain examples of different [protocols](https://docs.canvasmedical.com/docs/canvas-cli#upload) that can be uploaded to Canvas environments to support clinical workflows. These protocols are calculated on specified [events](https://docs.canvasmedical.com/docs/event-types) emitted from the canvas platform (you can choose whatever event you want to listen for).

Here are examples of different protocols you can find in this repo:

- On appointment creation, create a task to remind patients of their upcoming appointment.
- On appointment update or creation, send a notification to an external server with relevant information about the appointment.
- On patient data change, show a protocol in each patient's chart with useful patient links for the clinical user.

For instructions on how to create, test, and upload protocols, please see our [documentation](https://docs.canvasmedical.com/docs/sdk-quickstart#initial-setup).

### Value Sets

[`canvas_workflow_helpers/value_sets`](https://github.com/canvas-medical/open-source-sdk/tree/main/canvas_workflow_helpers/value_sets) contains the [v2021 value sets](https://docs.canvasmedical.com/docs/value-sets). Value sets contain lists of codes (RXNORM, SNOMED, ICD...) that represent concepts. An example of a custom value set is as follows:

```
class Nausea(ValueSet):
    VALUE_SET_NAME = 'Nausea with vomiting, unspecified'
    ICD10CM = {'R112'}
```

This Nausea value set may be used in many different scenarios. Here is one example of its use:

```
def affected_population(self):
    """  Patients with nausea.  """
    nausea_conditions = self.patient.conditions.find(Nausea).filter(clinicalStatus='active')
    if not nausea_conditions:
        return False
    return True
```

The v2021 value sets are maintained by the [Agency for Healthcare Research and Quality](https://www.hcup-us.ahrq.gov/) (or AHRQ) and is updated throughout the year to return the most up-to-date results. Some scenarios may require a custom value set not present in the v2021 set.

:construction: **_Note_** :construction:
We are working on making this open source repo a project on PyPI. Once `open-source-sdk` is a project on PyPI, any custom value set merged into the repository can be imported and used in any protocol.
Until then, this is how you can import v2021 value sets:

```
from canvas_workflow_sdk.value_set.v2021 import Hba1CLaboratoryTest
```

For more documentation on the v2021 value sets, see our [documentation](https://docs.canvasmedical.com/docs/value-sets).

---

We encourage developers to fork this repo and share their custom protocols and Value Sets. The `canvas-workflow-kit` gives developers the flexibility to implement a variety of custom workflows; imagine what we could do if we shared them all!

## Getting Started

At Canvas Medical, we use [Poetry](https://python-poetry.org/) for packaging and dependency management. Please follow the documentation to _install Poetry_.

**_Fork this repo_** then clone it into a directory named `open-source-sdk`

from the `open-source-sdk` directory run

```
$ poetry install
```

By default Poetry creates a virtual environment with all of the project dependencies.
To use the installed dependencies, activate the new environment by running

```
$ poetry shell
```

Verify the `canvas-workflow-kit` command options once you are in the poetry shell by running

```
(env)$ canvas-cli
```

Please follow the configuration instructions found in the [documentation](https://docs.canvasmedical.com/docs/canvas-cli#settings) to make sure you can submit to your Canvas instance using `canvas-cli`.

The protocol examples found in [`open-source-sdks/canvas_workflow_helpers/protocols`](https://github.com/canvas-medical/open-source-sdk/tree/main/canvas_workflow_helpers/protocols) can all be uploaded to your canvas instance by running

```
(env)$ cd canvas_workflow_helpers/protocols
(env)$ canvas-cli upload FILENAME
```

All documentation and details on each protocol are available [here](https://docs.canvasmedical.com/docs/protocol-examples).
We hope these examples can provide more insight into building your protocols.

You can use any of the value sets found in [`open-source-sdks/canvas_workflow_helpers/value_sets`](https://github.com/canvas-medical/open-source-sdk/tree/main/canvas_workflow_helpers/value_sets) by importing them into your protocols like this:

```
from canvas_workflow_sdk.value_set.v2021 import Hba1CLaboratoryTest
```

To get out of the poetry shell just enter `exit`

## Contributing

Please review our [Contributing Guidelines](https://github.com/canvas-medical/open-source-sdk/blob/main/CONTRIBUTING.md) and [Code of Conduct](https://github.com/canvas-medical/open-source-sdk/blob/main/CODE_OF_CONDUCT.md) before contributing to this open source repo.
