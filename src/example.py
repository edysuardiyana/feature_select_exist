from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2


def main():
    iris = load_iris()
    X, y = iris.data, iris.target
    k_value = 
    X_new = SelectKBest(chi2, k=)
    X_new.fit_transform(X, y)
    X_new.get_support()

    print "This is X: "
    print X

    print "This is X_new get support:"
    print X_new.get_support()
if __name__ == "__main__":
    main()
