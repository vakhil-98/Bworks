## Contributing

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

## Welcome

New project contributors are always welcome, and we are pleased to have them. Please feel free to ask any questions you may have in the project's forum or chat room.

You may make sure that your project is inviting to contributors and that you benefit the most from their efforts by adhering to these rules.

## Committers!
--------------
 * Code is peer reviewed, you should (almost) never push your own code.
 * Please don't accidentally force push to master.
 * Cherry Pick / Rebase commits, *don't use the big green button*, see below for instructions on how to
 merge a pull request.
 * Ensure reviewed code follows the above contribution guidelines, if it doesn't feel free to amend and make note.
 * Please try to watch when Pull Requests are made and review and / or commit them in a timely manner.
 * After you merge in a patch use tin to update the version accordingly. Run `tin -v x.x.x-prerelease` with x.x.x being the previous version upgraded appropriately via semver. When we are ready to publish to npm we can remove the `-prerelease`.
 * Thanks, you are all awesome human beings.

*How to merge a pull request*
 * Go to the pouchdb repository on your machine
 * Get the link to the patch of the pull request, which can be found under 'view command line instructions'
 next to the green 'Merge pull request' button on the page on GitHub for the pull request
 * Close the pull request once it has been merged, so no-one accidentally tries to merge it themselves
 * Make sure the issue associated with the pull request is closed, if the issue was resolved by that pull
 request
