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

Run the Workflow `fashion-mnist.yaml` in the usual way Workflows are run on Gradient:

 - Clone this repo to your machine: `git clone https://github.com/gradient-ai/Deployments`
 - Create a Project `Fashion MNIST` and get its ID
 - Create a Workflow `fashion-mnist` within the Project, and get its ID
 - Create a Dataset `fashion-mnist` within the Project
 - Invoke the Workflow on the command line: `gradient workflows run --id <Your Workflow ID> --path fashion-mnist.yaml`

For information on creating Projects, Workflows, Datasets, and setting up the CLI, refer to the [Gradient documentation](https://docs.paperspace.com/gradient/) or [tutorials](https://docs.paperspace.com/gradient/get-started/tutorials-list).

### 2. Deploy the model using Deployments

This deploys the model from step 1 and makes it ready to receive inference data.

 - Add the model ID from the trained model in step 1 to your copy of the model spec file `fashion-mnist-spec.yaml` from the cloned repo
 - Invoke the Deployment from the command line: `gradient deployments create --name fashion-mnist --projectId <Your Project ID> --spec fashion-mnist-deployment-spec.yaml`

The resulting deployment is visible in the GUI under the Deployments tab for your project.
 
### 3. Send inference data to the model

We need to send 784x784 pixel Fashion-MNIST images to the model, so this is more easily done by script than on the command line.
 
We therefore call the script using another Workflow:

 - Create Workflow `fashion-mnist-infer` within your Project, and get its ID
 - Invoke the Workflow in the same way as step 1, but with the Workflow ID and YAML file for this step: `gradient workflows run --id <Your Workflow ID> --path fashion-mnist-infer.yaml`

For this inference data, the true classes are also available, so the output will show the true class and the model's predicted class for each image. They should be mostly the same.

## Next Steps

Gradient Deployments contain more than shown here, and we are rapidly adding functionality. 

In future material what we plan to show includes:

- Create deployment in a Workflow
- Invoke deployment via SDK
- Deployment metrics
- Canary deployments
- Trigger deployment via our GitHub-repo-linked projects

For more details about what is current supported in Deployments, see the [documentation](https://docs.paperspace.com/gradient/explore-train-deploy/deployments).
