## Contributing to Canvas Medical

:sparkles: First off, thanks for taking the time to contribute! :sparkles:

We do not intend to make representations or warranties regarding workflow experiences. We understand that each practice may have individual requirements for their Canvas instance. We want to empower external developers to customize and share their unique solutions to individualize their Canvas experience.

## Code of Conduct

The Canvas Medical [Code of Conduct](https://github.com/canvas-medical/open-source-sdk/blob/main/CODE_OF_CONDUCT.md) governs this project and everyone participating. By participating, you are expected to uphold this code.

You understand that these Contributing Guidelines, our Code of Conduct, and any license terms that we provide with open source materials (collectively “Open Source Terms”), are specific to the materials available through the Canvas Medical Open Source Project only. Under no circumstances will any of the Open Source Terms apply to Canvas Medical’s products and services generally. Unless materials are specifically identified as “Open Source”, materials available through the Canvas Medical website are subject to our general [Terms of Use](https://www.canvasmedical.com/terms-of-use) or our [License Agreement](https://www.canvasmedical.com/license-agreement).

Please never include any PHI when submitting examples. Revealing PHI would directly violate our Code of Conduct and would result in your dismissal from the project. If you find any security vulnerabilities relating to PHI or encounter unacceptable behavior, please report them directly to community-engagement@canvasmedical.com rather than opening a new issue.

## What should I know before I get started?

Canvas Medical open source is designed to support developers customizing their Canvas instances. At present, this open source project is meant to support users of the [canvas-workflow-kit](https://docs.canvasmedical.com/docs/sdk-quickstart).

You understand that by contributing work to the Canvas Medical Open Source project (“Contributions”), those Contributions become a part of the Canvas Medical Open Source project, and that we may use your Contributions without limitation, including to modify or improve Canvas Medical’s existing products or services, or to create new products or services. If we choose to incorporate any of your Contributions into Canvas Medical’s products or services, you understand that you will have no rights to those new or improved products or services, and that in no way are we required to relicense products or services into which we incorporate Contributions on any Open Source Terms.

## How Can I Contribute?

There are many ways to contribute, from writing tutorials or blog posts, improving the documentation, submitting workflow and feature requests, or writing code that can be incorporated into the open source branch of Canvas Medical.

Please, don't use the issue tracker for support questions. Please check existing Issues, Pull requests, and Projects before submitting a new Issue or PR.

We want to encourage users to do the following to share their unique protocol and workflow solutions:

- Create your own fork of the code.
- Do the changes in your fork.
- If you like the change and think the project could use it:
  - Be sure you have followed the code style for the project.
  - Be sure to review the [Code of Conduct](https://github.com/canvas-medical/open-source-sdk/blob/main/CODE_OF_CONDUCT.md).
  - Send a pull request indicating that you have read and acknowledged the Code of Conduct. Please be sure to use the [PR template](https://github.com/canvas-medical/open-source-sdk/blob/main/.github/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md) provided. We also request that your code be well tested. All existing and new tests must pass before requesting review.

If you would like to submit a workflow or feature request as an issue, please use the [Issue template](https://github.com/canvas-medical/open-source-sdk/blob/main/.github/ISSUE_TEMPLATE/ISSUE_TEMPLATE.md) provided.

### Before Submitting An Workflow/Feature Suggestion

Check the [Canvas Medical docs](https://docs.canvasmedical.com/docs/introduction) for tips — you might discover that the feature is already available. Most importantly, check if you're using the latest version of the [Canvas Medical SDK](https://pypi.org/project/canvas-workflow-kit/).
Check if there's already a [protocol example](https://github.com/canvas-medical/open-source-sdk/tree/main/canvas_workflow_helpers/protocols) that provides that workflow.
Perform a cursory search to see if the workflow has already been suggested. If it has, add a comment to the existing issue instead of opening a new one.

## Style Guides

At Canvas Medical, we follow [Django best practices](https://django-best-practices.readthedocs.io/en/latest/code.html), use [yapf](https://github.com/google/yapf) as a formatter, and use flake8 for linting.
