## Contributing

## Welcome

New project contributors are always welcome, and we are pleased to have them. Please feel free to ask any questions you may have in the project's forum or chat room.

You may make sure that your project is inviting to contributors and that you benefit the most from their efforts by adhering to these rules.

### Any contributions are welcome, including the following:
+ Code
+ Documentation
+ Bug Reports
+ Feature requests

### Please follow these steps to contribute:
+ Fork the project on GitHub.
+ Create a new branch for your changes.
+ Make your changes and commit them.
+ Push your changes to your branch.
+ Publish a pull request for the main branch.
+ If your pull request adheres to our criteria, we'll review it and merge it.

## Expectations
All contributions must adhere to the following requirements, at a minimum:
+ The code needs to be carefully written and tested.
+ The documentation needs to be concise and clear.
+ The bug reports need to be precise and reproducible.
+ The feature requests must be well-defined and feasible.

## Dependencies
The BWorks Donation Application has the following main dependencies:

- Node.js: A JavaScript runtime environment.

You can find a complete list of dependencies in the `package.json` file.

## CI/CD Pipeline

The BWorks Donation Application has a CI/CD pipeline defined in the `.github/workflows/ci-cd.yml` file. This pipeline is triggered on pull requests to the main branch and pushes to the `workflow` branch.

The pipeline consists of the following jobs:

1. *Test*: This job runs the application's tests to ensure the code meets the expected behavior.

2. *Lint*: This job checks the codebase for linting issues and ensures code quality and style consistency.

3. *Release*: This job is triggered when a commit message starts with the letter 'v', indicating a version release. It builds the application, runs tests, packages the code, and publishes the release.

The CI/CD pipeline helps automate the process of building, testing, and releasing the BWorks Donation Application, ensuring the stability and quality of the codebase.

## Testing

The BWorks Donation Application uses automated tests to verify the correctness of the code. Tests are written using a testing framework and can be found in the `tests/` directory.

To run the tests locally, use the following command:

bash
$ npm test

The tests will be executed, and the results will be displayed in the console.

## Road map for Contribution
![IMG_0305](https://github.com/anees1203/BWorks-Material-Donation-Tracking/assets/86214595/786fbd9f-fa61-427b-9420-e0caee928fd5)

## Feature Suggestions:

* Multilingual support: Allowing the project to be accessible to users from different geographical and cultural locations. To accomplish this, language files need to be added, localization is implemented, and a user interface to change languages is provided.

* Mobile app compatibility:  If possible, by creating a mobile version of the project to extend its reach and provide users with a seamless experience across different devices. This could involve developing native mobile apps or implementing responsive design for mobile web browsers.

* Notification system: By enabling a notification system that keeps users informed about important events or updates within the project, such as new messages, task assignments, or changes to shared content.

* Workflow automation: In order to improve productivity and save the user’s time the streamline and automate repetitive tasks or workflows within the project is much valued such as automated email notifications, batch processing, or task scheduling. This can improve productivity and save users' time.

* Customizable Dashboard: Provide users with the ability to customize their dashboard layout and content according to their preferences. This can involve allowing users to rearrange widgets, choose which data to display, and create personalized shortcuts for frequently accessed features.

## Committers!
 * Code is peer reviewed, you should (almost) never push your own code.
 * Please don't accidentally force push to master.
 * Cherry Pick / Rebase commits, *don't use the big green button*, see below for instructions on how to merge a pull request.
 * Ensure reviewed code follows the above contribution guidelines, if it doesn't feel free to amend and make note.
 * Please try to watch when Pull Requests are made and review and / or commit them in a timely manner.
 * Thanks, you are all awesome human beings.

*How to merge a pull request*
 * Go to the bworks repository on your machine
 * Get the link to the patch of the pull request, which can be found under 'view command line instructions' next to the green 'Merge pull request' button on the page on GitHub for the pull request
 * Close the pull request once it has been merged, so no-one accidentally tries to merge it themselves
 * Make sure the issue associated with the pull request is closed, if the issue was resolved by that pull request

