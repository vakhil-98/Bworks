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

## Getting Started

To get started with the BWorks Application, follow these steps:

1. Clone the BWorks repository:

$ git clone https://github.com/vakhil-98/Bworks.git

2. Install the project dependencies:

$ npm install

3. Start the development server:

$ npm start

You can now access the BWorks Donation Application in your web browser at `http://localhost:4200`.

## Development Workflow

The BWorks Donation Application follows a typical development workflow using Git. Here's a recommended workflow for contributing to the project:

1. Create a new branch for your feature or bug fix:

$ git checkout -b my-feature

2. Make the necessary changes to the codebase.

3. Commit your changes with a descriptive message:

$ git commit -m "Implement feature XYZ"

4. Push your branch to the remote repository:

$ git push origin my-feature

5. Open a pull request on GitHub to merge your changes into the main branch.

6. Discuss and review the pull request with other contributors.

7. Once your changes have been reviewed and approved, they can be merged into the main branch.


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


## Release Process
The release process is a critical phase in the project lifecycle that ensures the deployment of stable and reliable software to users. This section outlines the steps and best practices for managing releases effectively.

### Versioning Scheme
To maintain a clear and consistent approach to versioning, we use [insert versioning scheme here]. The version number typically consists of three parts: major version, minor version, and patch version. Here's a brief explanation of each component:

Major Version: Represents significant milestones or major feature releases. A change in the major version indicates possible breaking changes and may require user adaptation.
Minor Version: Signifies the addition of new features or enhancements that are backward compatible with the previous version.
Patch Version: Denotes bug fixes, patches, or minor updates that don't introduce new features and maintain backward compatibility.

### Release Branching Strategy
We follow the [insert branching strategy here] branching strategy for managing releases. This strategy ensures a structured and controlled approach to releasing new features and bug fixes. The key branches involved in the release process are:

Main/Branch: Represents the production-ready codebase. Only stable and thoroughly tested code should be merged into this branch.
Application/Branch: Acts as the integration branch for ongoing development. Feature branches are merged into this branch for testing and review.

### Release Workflow
The release workflow consists of several steps to ensure a smooth and reliable release process. Here's an overview of the typical workflow:

* Feature Development: Developers work on new features or bug fixes in separate feature branches, branching off from the development branch.
Feature Testing: Each feature branch undergoes thorough testing, including unit tests, integration tests, and any relevant automation tests.
* Code Review: All feature branches must go through a code review process to ensure code quality, adherence to coding standards, and best practices.
* Integration: Once a feature branch passes the code review, it is merged into the development branch for integration testing.
* Release Candidate: When the development branch is considered stable, a release branch is created from it. This branch is dedicated to finalizing the release candidate.
* Testing: The release candidate is thoroughly tested to identify and fix any remaining issues or bugs.
Documentation Update: Update the project documentation, including release notes, user guides, and any other relevant documentation to reflect the changes and new features introduced in the release.
* Release Approval: The release candidate is reviewed by the project stakeholders, including product managers and QA teams, to ensure it meets the required quality standards.
* Merge to Main: Once the release candidate is approved, it is merged into the main branch, triggering the official release process.
* Deployment: The release is deployed to the production environment following the defined deployment process and any relevant infrastructure automation.
* Post-Release Tasks: Conduct post-release activities such as monitoring, bug tracking, user feedback collection, and performance analysis to address any issues that arise.

### Release Documentation
Clear and comprehensive release documentation is crucial for providing users and stakeholders with information about the release and its impact. The following information should be included in the release documentation:

* Release version and date
* Overview of new features, enhancements, and bug fixes
Known issues and limitations
* Upgrade instructions, if applicable
* Contact information for support or feedback
  
It is important to maintain an organized and accessible repository of release documentation, making it easy for users to access information about previous releases.





