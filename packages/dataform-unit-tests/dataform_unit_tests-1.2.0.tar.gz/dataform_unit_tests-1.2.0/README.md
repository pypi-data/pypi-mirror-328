# dataform-unit-testing

This package contains Python code that is executed as part of GitHub Actions pipelines in Dataform-enabled projects to perform unit tests on Dataform models:

 - Asserts that any defined unit test validates the behaviour of any relevant Dataform models.
 - Presents any issues with Dataform code identified.
 - If any issues detected, fails the CI/CD pipeline
