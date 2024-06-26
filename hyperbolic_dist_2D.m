function d = hyperbolic_dist_2D(XI, XJ)
%Computes the hyperbolic distance between point XI (1 x 2) and the m points
%stored in XJ (m x 2). The coordinates of these points are polar in the
%format (angular coord, radial coord). The resulting similarities are
%stored in d.
%
%INPUT
%   XI -> The polar coordinates of a single point in the Poincaré disc.
%   XJ -> The polar coordinates of m points in the Poincaré disc.
%
%OUTPUT
%   d -> The hyperbolic distance between point XI and the other m points
%        stored in XJ. The hyperbolic distance between points (Ti, Ri) and
%        (Tj, Rj) in the hyperbolic space H^2 of curvature K = -1,
%        represented by the Poincaré disc is:
%
% Dij = arccosh(cosh(Ri)*cosh(Rj) - sinh(Ri)*sinh(Rj)*cos(Tij));
%
%        with Tij = pi - |pi - |Ti - Tj||
%
% Copyright (C) Gregorio Alanis-Lobato, 2014

A =  pi - abs(pi - abs(XI(1) - XJ(:,1))); %angular separation between points
d = acosh(cosh(XI(2)).*cosh(XJ(:,2)) - sinh(XI(2)).*sinh(XJ(:,2)).*cos(A));
d(isinf(d)) = 0;

% due to numerical approximations, points with a tiny or zero angular
% separation and close radial coordinates could produce a wrong complex
% hyperbolic distance with zero real part. These distances are replaced
% by the radial separation as expected by the theoretical formula.
if ~isreal(d)
   d(imag(d)~=0) = abs(XI(2)-XJ(imag(d)~=0,2)); 
end
end
