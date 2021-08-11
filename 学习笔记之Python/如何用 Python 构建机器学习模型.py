""" LinearRegression """

# Import modules
from sklearn import linear_model

# Create training and test subsets
x_train = train_dataset_predictor_variables
y_train = train_dataset_predicted_variable

x_test  = test_dataset_precictor_variables

# Create linear regression object
linear = linear_model.LinearRegression()

# Train the model with training data and check the score
linear.fit(x_train, y_train)
linear.score(x_train, y_train)

# Collect coefficients
print('Coefficient: \n', linear.coef_)
print('Intercept: \n', linear.intercept_)

# Make predictions
predicted_values = linear.predict(x_test)

""" LogisticRegression """

# Import modules
from sklearn.linear_model import LogisticRegression

# Create training and test subsets
x_train = train_dataset_predictor_variables
y_train = train_dataset_predicted_variable

x_test  = test_dataset_precictor_variables

# Create logistic regression object
model = LogisticRegression()

# Train the model with training data and checking the score
model.fit(x_train, y_train)
model.score(x_train, y_train)

# Collect coefficients
print('Coefficient: \n', model.coef_)
print('Intercept: \n', model.intercept_)

# Make predictions
predicted_vaues = model.predict(x_teste)

""" DecisionTreeRegressor """

# Import modules
from sklearn import tree

# Create training and test subsets
x_train = train_dataset_predictor_variables
y_train = train_dataset_predicted_variable

x_test  = test_dataset_precictor_variables

# Create Decision Tree Regressor Object
model = tree.DecisionTreeRegressor()

# Create Decision Tree Classifier Object
model = tree.DecisionTreeClassifier()

# Train the model with training data and checking the score
model.fit(x_train, y_train)
model.score(x_train, y_train)

# Make predictions
predicted_values = model.predict(x_test)

""" GaussianNB """

# Import modules
from sklearn.naive_bayes import GaussianNB

# Create training and test subsets
x_train = train_dataset_predictor_variables
y_train = train_dataset_predicted variable

x_test  = test_dataset_precictor_variables

# Create GaussianNB object
model = GaussianNB()

# Train the model with training data
model.fit(x_train, y_train)

# Make predictions
predicted_values = model.predict(x_test)

""" svm """

# Import modules
from sklearn import svm

# Create training and test subsets
x_train = train_dataset_predictor_variables
y_train = train_dataset_predicted variable

x_test  = test_dataset_precictor_variables

# Create SVM Classifier object
model = svm.svc()

# Train the model with training data and checking the score
model.fit(x_train, y_train)
model.score(x_train, y_train)

# Make predictions
predicted_values = model.predict(x_test)

""" KNeighborsClassifier """

# Import modules
from sklearn.neighbors import KNeighborsClassifier

# Create training and test subsets
x_train = train_dataset_predictor_variables
y_train = train_dataset_predicted variable

x_test  = test_dataset_precictor_variables

# Create KNeighbors Classifier Objects
KNeighborsClassifier(n_neighbors = 6) # default value = 5

# Train the model with training data
model.fit(x_train, y_train)

# Make predictions
predicted_values = model.predict(x_test)

""" KMeans """

# Import modules
from sklearn.cluster import KMeans

# Create training and test subsets
x_train = train_dataset_predictor_variables
y_train = train_dataset_predicted variable

x_test  = test_dataset_precictor_variables

# Create KMeans objects
k_means = KMeans(n_clusters = 3, random_state = 0)

# Train the model with training data
model.fit(x_train)

# Make predictions
predicted_values = model.predict(x_test)

""" RandomForestClassifier """

# Import modules
from sklearn.ensemble import RandomForestClassifier

# Create training and test subsets
x_train = train_dataset_predictor_variables
y_train = train_dataset_predicted variable

x_test  = test_dataset_precictor_variables

# Create Random Forest Classifier objects
model = RandomForestClassifier()

# Train the model with training data
model.fit(x_train, x_test)

# Make predictions
predicted_values = model.predict(x_test)

""" decomposition """

# Import modules
from sklearn import decomposition

# Create training and test subsets
x_train = train_dataset_predictor_variables
y_train = train_dataset_predicted variable

x_test  = test_dataset_precictor_variables

# Creating PCA decomposition object
pca = decomposition.PCA(n_components = k)

# Creating Factor analysis decomposition object
fa = decomposition.FactorAnalysis()

# Reduc the size of the training set using PCA
reduced_train = pca.fit_transform(train)

# Reduce the size of the training set using PCA
reduced_test = pca.transform(test)

""" GradientBoostingClassifier """

# Import modules
from sklearn.ensemble import GradientBoostingClassifier

# Create training and test subsets
x_train = train_dataset_predictor_variables
y_train = train_dataset_predicted variable

x_test  = test_dataset_precictor_variables

# Creating Gradient Boosting Classifier object
model = GradientBoostingClassifier(n_estimators = 100, learning_rate = 1.0, max_depth = 1, random_state = 0)

# Training the model with training data
model.fit(x_train, x_test)

# Make predictions
predicted_values = model.predict(x_test)
