
from sklearn.datasets import fetch_20newsgroups
from sklearn.metrics.metrics import f1_score, classification_report
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import Perceptron

categories = ['rec.sport.hockey', 'rec.sport.baseball', 'rec.autos']
newsgroups_train = fetch_20newsgroups(subset='train', categories=categories, remove=('headers', 'footers', 'quotes'))
newsgroups_test = fetch_20newsgroups(subset='test', categories=categories, remove=('headers', 'footers', 'quotes'))

vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(newsgroups_train.data)
X_test = vectorizer.transform(newsgroups_test.data)

classifier = Perceptron(n_iter=100, eta0=0.1)
classifier.fit_transform(X_train, newsgroups_train.target)
predictions = classifier.predict(X_test)
print classification_report(newsgroups_test.target, predictions)


################# Example #################

import numpy as np
import matplotlib
matplotlib.use('Qt4Agg')
import matplotlib.pyplot as plt
from sklearn.linear_model import Perceptron

X = np.array([
    [1, 0.2, 0.1],
    [1, 0.4, 0.6],
    [1, 0.5, 0.2],
    [1, 0.7, 0.9]
])
# X = np.array([
#     [1, 0, 0],
#     [1, 0, 1],
#     [1, 1, 0],
#     [1, 1, 1]
# ])
Y = np.array([1, 1, 1, 0])
h = .01  # step size in the mesh
threshold = 0.5
learning_rate = 0.1
weights = [0, 0, 0]
n_epochs = 10


def predict(x, weights):
    weighted_sum = np.dot(x, weights)
    if weighted_sum > threshold:
        return 1
    return 0


def get_activation_string(x, weights):
    l = []
    for i, v in enumerate(x):
        l.append('%s*%s' % (v, weights[i]))
    s = ' + '.join(l) + ' = ' + str(np.dot(x, weights))
    return s


def predict_with_bias(x, weights):
    Z = []
    for i in x:
        biased = np.hstack(([1], i))
        weighted_sum = np.dot(biased, weights)
        if weighted_sum > threshold:
            Z.append(1)
        else:
            Z.append(0)
    return np.array(Z)


x_min, x_max = -0.4, 1.4
y_min, y_max = -0.4, 1.4
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

plot_num = 1
for epoch in range(1, n_epochs):
    print 'Epoch', epoch
    print 'Instance;Initial Weights;x;Activation;Prediction;Target;Correct;Updated Weights'
    converged = True
    for i in range(len(X)):
        previous_weights = np.array(weights)
        prediction = predict(X[i], weights)
        correct = True
        if prediction != Y[i]:
            correct = False
            converged = False
            correction = -1
            if Y[i] == 1:
                correction = 1
            weights += X[i] * learning_rate * correction
        print '%s;%s;%s;%s;%s;%s;%s;%s' % (
            i,
            ', '.join([str(w) for w in previous_weights]),
            ', '.join([str(x) for x in X[i]]),
            get_activation_string(X[i], previous_weights),
            prediction, Y[i], correct,
            ', '.join([str(w) for w in weights]))
                # Plot the decision boundary and the instances
        plt.subplot(9, 4, plot_num)
        Z = predict_with_bias(np.c_[xx.ravel(), yy.ravel()], weights)
        Z = Z.reshape(xx.shape)
        plt.contourf(xx, yy, Z, cmap=plt.cm.Paired)
        plt.scatter(X[:, 1], X[:, 2], c=Y, cmap=plt.cm.Paired)
        # plt.axis('off')
        plt.xlim((-0.2, 1.2))
        plt.ylim((-0.2, 1.2))
        plot_num += 1
    if converged:
        print 'Converged during epoch %s!' % epoch
        break

# Plot the decision boundary and the instances
plt.figure()
plt.title('Perceptron Decision Boundary')
Z = predict_with_bias(np.c_[xx.ravel(), yy.ravel()], weights)
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, cmap=plt.cm.Paired)
plt.scatter(X[:, 1], X[:, 2], c=Y, cmap=plt.cm.Paired)
# plt.axis('off')
plt.xlim((-0.2, 1.2))
plt.ylim((-0.2, 1.2))
plot_num += 1
plt.show()
