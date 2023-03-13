%  0: 'airplane',
%  1: 'automobile',
%  2: 'bird',
%  3: 'cat',
%  4: 'deer',
%  5: 'dog',
%  6: 'frog',
%  7: 'horse',
%  8: 'ship',
%  9: 'truck',


%%%load cifar10
load cifar10_data_batch_1.mat
% combine two table
cifar = [data labels];
% sort the table by labels
cifarSort = sortrows(cifar, 3073);
% I deal with the data in the excel
xlswrite('D:\data.xlsx',cifarSort)
% pick the 0,2,4,5 classes
% make the dataset to 'cifar.mat'
% load the dataset
load cifar
% separate dataset to data and labels
cifar4 = cifar(:, 1:end-1);
labels4 = cifar(:, end);
% disrupt the order
rowrank = randperm(size(cifar4, 1));
cifar4 = cifar4(rowrank,:);
labels4 = labels4(rowrank,:);
% pca
[coeff4,score4,latent4] = pca(double(cifar4), 'NumComponents', 2);
% plot graph
Ce = {};
figure; 
hold on;
for i = 1:4
    Ce{i} = score4(labels4==i-1, :);
    scatter ( Ce{i} (:, 1) , Ce{i} (:, 2),25, '*');
end
legend({'0:airplane', '2:bird','4:deer', '5:dog'});
xlabel('First Principle Component');
ylabel('Second Principle Component');

