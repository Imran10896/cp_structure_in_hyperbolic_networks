function [x,coords,d] = generateS1Model(N, k_avg, gamma, alpha)
% Parameters
kappa0 = (gamma - 2) / (gamma - 1) * k_avg;
% Step 1: Generate angular coordinates
theta = 2 * pi * rand(1, N);
% Step 2: Generate hidden variables
kappa = kappa0 * (1-rand(1, N)).^(1 / (1 - gamma));
mu = (alpha * sin(pi / alpha)) / (2 * pi * k_avg);
R = 2 * log(N/(pi*mu*((kappa0).^2)));
for i=1:N
r(i) = R-2*log(kappa(i)/kappa0);
end
% Step 3: Generate candidate edges and calculate probabilities
candidateEdges = nchoosek(1:N, 2);
numCandidateEdges = size(candidateEdges, 1);
probabilities = zeros(numCandidateEdges, 1);
for edgeIdx = 1:numCandidateEdges
i = candidateEdges(edgeIdx, 1);
j = candidateEdges(edgeIdx, 2);
delta_theta = pi - abs(pi - abs(theta(i) - theta(j)));
prob_connect = 1 / (1 + (N * delta_theta) / (2 * pi * mu * kappa(i) * kappa(j))^alpha);
probabilities(edgeIdx) = prob_connect;
end
% Step 4: Use datasample to choose edges based on probabilities
chosenEdgesIdx = datasample(1:numCandidateEdges, round((N*k_avg)/2), 'Weights', probabilities);
x = zeros(N, N);
coords(:,1)=theta';
coords(:,2)=r';
for edgeIdx = chosenEdgesIdx
i = candidateEdges(edgeIdx, 1);
j = candidateEdges(edgeIdx, 2);
x(i, j) = 1;
x(j, i) = 1;
end
d = zeros(N);
for i=1:N
    for j=1:N
        d(i,j)=1/(1+hyperbolic_dist_2D(coords(i,1:2),coords(j,1:2)));
    end
end
end
