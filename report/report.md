---
title: COMP6211D PA3 Report
author: NIU Zhe (20526438)
---

# Vanilla GAN

## Hyperparameters

| Hyperparameter | Value  |
| -------------- | ------ |
| batch_size     | 16     |
| beta1          | 0.5    |
| beta2          | 0.999  |
| conv_dim       | 32     |
| emoji          | Apple  |
| image_size     | 32     |
| lr             | 0.0003 |
| noise_size     | 100    |
| num_epochs     | 60     |


## Image Samples

![](../samples_vanilla/sample-001000.png){width=4cm}
![](../samples_vanilla/sample-004200.png){width=4cm}
![](../samples_vanilla/sample-008400.png){width=4cm}

\begin{figure}[!h]
\centering
\caption{From left to right are iteration 1000, 4200, 8400. The image quality is bad at iteration 1000 with many blur, and getting better at iteration 4200. Iteration 8400 is more clear than iteration 4200, but some faces get disorted.}
\end{figure}

## Loss Curve

![Vanilla GAN loss curve. The generator has higher loss throughout the training.](fig/vanilla_gan.png){width=13cm}
 

# CycleGAN

## Hyperparameters

| Hyperparameter | Value   |
| -------------- | ------- |
| image_size     | 32      |
| g_conv_dim     | 32      |
| d_conv_dim     | 32      |
| train_iters    | 10000   |
| batch_size     | 16      |
| lr             | 0.0003  |
| beta1          | 0.5     |
| beta2          | 0.999   |
| X              | Apple   |
| Y              | Windows |


## Image Samples


![Apple to Windows: Bad Quality.](../samples_cyclegan/sample-000500-X-Y.png){width=6cm}\ ![Windows to Apple: Bad Quality.](../samples_cyclegan/sample-000500-Y-X.png){width=6cm}

\begin{figure}[!h]
\centering
\caption{After 500 iterations, the model can generate some blur images.}
\end{figure} 

![Apple to Windows Good Quality.](../samples_cyclegan/sample-004000-X-Y.png){width=6cm}\ ![Windows to Apple Good Quality.](../samples_cyclegan/sample-004000-Y-X.png){width=6cm}

\begin{figure}[!h]
\centering
\caption{After around 4000 iterations, the generated images have better quality.}
\end{figure}


![Apple to Windows: Bad Quality.](../samples_cyclegan/sample-010000-X-Y.png){width=6cm}\ ![Windows to Apple: Bad Quality.](../samples_cyclegan/sample-010000-Y-X.png){width=6cm}

\begin{figure}[!h]
\centering
\caption{After 10000 iterations, the model seems trapped into some local minimal. The generators are trying to add some noise on the original image to fake the style so that it can fool the discriminator.}
\end{figure}

## Loss Curve

![CycleGAN loss curve, the generator has higher loss thoughtout the training. There are some spikes during the training, this may be caused by the bad training samples, whose distribution are very different from the previous smaples.](fig/cycle_gan.png){width=13cm}
