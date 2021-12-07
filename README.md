# Deployments

Last updated: Dec 07th 2021

This is our basic example of Deployments in Gradient, showing how to

 - Create and train a TensorFlow deep learning model using Workflows
 - Deploy the model using Deployments
 - Send inference data to the model and receive correct output

A key component of this is to show that *models created in Gradient can be deployed in Gradient*.

## See also

- Blog entry
- Deployments documentation

## How to run

### 1. Create TensorFlow model

This creates a TensorFlow 2.6 model using the Fashion-MNIST dataset. Our purpose here is to show working deployments so we do not attempt anything large or complicated.

Run the Workflow fashion-mnist.yaml in the usual way Workflows are run on Gradient:

 - Clone this repo
 - Create Project
 - Create Workflow and get its ID
 - Create output Dataset
 - Invoke the Workflow on the command line: `gradient workflows run --id <Workflow ID> --path fashion-mnist.yaml`

### 2. Deploy the model using Deployments

This deploys the model from step 1 and makes it ready to receive inference data.

 - Add model ID from step 1 to the model spec file `fashion-mnist-spec.yaml`
 - Invoke the Deployment from the command line: `gradient deployments create --name fashion-mnist --projectId <Project ID> --spec fashion-mnist-deployment-spec.yaml`

The resulting deployment is visible in the GUI under the Deployments tab for your project.
 
### 3. Send inference data to the model

We need to send 784*784 pixel Fashion-MNIST images to the model, so this is more easily done by script than on the command line.
 
We therefore call the script using another Workflow:

 - Create Workflow and get its ID
 - Invoke the Workflow in the same way as step 1, but with the YAML file for this step: `gradient workflows run --id <Workflow ID> --path fashion-mnist-inference.yaml`

For this inference data, the true classes are also available, so the output will show the true class and the model's predicted class for each image.

## Next Steps

Gradient Deployments contain more than shown here, and we are rapidly adding functionality. In future material we plan to show

- Create deployment in a Workflow
- Invoke deployment via SDK
- Deployment metrics
- Canary deployments
- Trigger deployment via our GitHub-repo-linked projects

For more details about what is current supported in Deployments, see the [documentation](https://docs.paperspace.com/gradient/explore-train-deploy/deployments).
