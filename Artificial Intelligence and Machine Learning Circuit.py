from sklearn.ensemble import IsolationForest
import pandas as pd

# قراءة البيانات من الشبكة
data = pd.read_csv('network_traffic.csv')

# تدريب نموذج IsolationForest للكشف عن التهديدات
model = IsolationForest(n_estimators=100, contamination=0.01)
model.fit(data)

# التنبؤ بالسلوك غير الطبيعي
anomalies = model.predict(data)
