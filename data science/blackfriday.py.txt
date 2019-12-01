In [14]:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
In [15]:
df=pd.read_csv('datasets/BlackFriday.csv')
In [16]:
df.head()
Out[16]:
User_ID	Product_ID	Gender	Age	Occupation	City_Category	Stay_In_Current_City_Years	Marital_Status	Product_Category_1	Product_Category_2	Product_Category_3	Purchase
0	1000001	P00069042	F	0-17	10	A	2	0	3	NaN	NaN	8370
1	1000001	P00248942	F	0-17	10	A	2	0	1	6.0	14.0	15200
2	1000001	P00087842	F	0-17	10	A	2	0	12	NaN	NaN	1422
3	1000001	P00085442	F	0-17	10	NaN	2	0	12	14.0	NaN	1057
4	1000002	P00285442	M	55+	16	C	4+	0	8	NaN	NaN	7969
In [17]:
df.describe()
Out[17]:
User_ID	Occupation	Marital_Status	Product_Category_1	Product_Category_2	Product_Category_3	Purchase
count	5.375770e+05	537577.00000	537577.000000	537577.000000	370591.000000	164278.000000	537577.000000
mean	1.002992e+06	8.08271	0.408797	5.295546	9.842144	12.669840	9333.859853
std	1.714393e+03	6.52412	0.491612	3.750701	5.087259	4.124341	4981.022133
min	1.000001e+06	0.00000	0.000000	1.000000	2.000000	3.000000	185.000000
25%	1.001495e+06	2.00000	0.000000	1.000000	5.000000	9.000000	5866.000000
50%	1.003031e+06	7.00000	0.000000	5.000000	9.000000	14.000000	8062.000000
75%	1.004417e+06	14.00000	1.000000	8.000000	15.000000	16.000000	12073.000000
max	1.006040e+06	20.00000	1.000000	18.000000	18.000000	18.000000	23961.000000
In [18]:
df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 537577 entries, 0 to 537576
Data columns (total 12 columns):
User_ID                       537577 non-null int64
Product_ID                    537577 non-null object
Gender                        537577 non-null object
Age                           537577 non-null object
Occupation                    537577 non-null int64
City_Category                 537452 non-null object
Stay_In_Current_City_Years    537577 non-null object
Marital_Status                537577 non-null int64
Product_Category_1            537577 non-null int64
Product_Category_2            370591 non-null float64
Product_Category_3            164278 non-null float64
Purchase                      537577 non-null int64
dtypes: float64(2), int64(5), object(5)
memory usage: 39.0+ MB
In [19]:
df.drop(['User_ID', 'Product_ID', 'Stay_In_Current_City_Years'], axis=1, inplace=True)
df.head()
Out[19]:
Gender	Age	Occupation	City_Category	Marital_Status	Product_Category_1	Product_Category_2	Product_Category_3	Purchase
0	F	0-17	10	A	0	3	NaN	NaN	8370
1	F	0-17	10	A	0	1	6.0	14.0	15200
2	F	0-17	10	A	0	12	NaN	NaN	1422
3	F	0-17	10	NaN	0	12	14.0	NaN	1057
4	M	55+	16	C	0	8	NaN	NaN	7969
In [20]:
df['City_Category']=df['City_Category'].fillna("X")
df.head()
Out[20]:
Gender	Age	Occupation	City_Category	Marital_Status	Product_Category_1	Product_Category_2	Product_Category_3	Purchase
0	F	0-17	10	A	0	3	NaN	NaN	8370
1	F	0-17	10	A	0	1	6.0	14.0	15200
2	F	0-17	10	A	0	12	NaN	NaN	1422
3	F	0-17	10	X	0	12	14.0	NaN	1057
4	M	55+	16	C	0	8	NaN	NaN	7969
In [21]:
df['City_Category']=df['City_Category'].map({'A':'Metro Cities', 'B':'Small Towns', 'C':'Villages', 'X' :'X' })
df.head()
Out[21]:
Gender	Age	Occupation	City_Category	Marital_Status	Product_Category_1	Product_Category_2	Product_Category_3	Purchase
0	F	0-17	10	Metro Cities	0	3	NaN	NaN	8370
1	F	0-17	10	Metro Cities	0	1	6.0	14.0	15200
2	F	0-17	10	Metro Cities	0	12	NaN	NaN	1422
3	F	0-17	10	X	0	12	14.0	NaN	1057
4	M	55+	16	Villages	0	8	NaN	NaN	7969
In [22]:
df.rename(columns={'Product_Category_1':'Baseball Caps','Product_Category_2':'Wine Tumblers' ,'Product_Category_3':'Pet Raincoats'},inplace=True)
df.head()
Out[22]:
Gender	Age	Occupation	City_Category	Marital_Status	Baseball Caps	Wine Tumblers	Pet Raincoats	Purchase
0	F	0-17	10	Metro Cities	0	3	NaN	NaN	8370
1	F	0-17	10	Metro Cities	0	1	6.0	14.0	15200
2	F	0-17	10	Metro Cities	0	12	NaN	NaN	1422
3	F	0-17	10	X	0	12	14.0	NaN	1057
4	M	55+	16	Villages	0	8	NaN	NaN	7969
In [23]:
df['Marital_Status']=df['Marital_Status'].map({1:'Married',0:'Un-Married'})
df.head()
Out[23]:
Gender	Age	Occupation	City_Category	Marital_Status	Baseball Caps	Wine Tumblers	Pet Raincoats	Purchase
0	F	0-17	10	Metro Cities	Un-Married	3	NaN	NaN	8370
1	F	0-17	10	Metro Cities	Un-Married	1	6.0	14.0	15200
2	F	0-17	10	Metro Cities	Un-Married	12	NaN	NaN	1422
3	F	0-17	10	X	Un-Married	12	14.0	NaN	1057
4	M	55+	16	Villages	Un-Married	8	NaN	NaN	7969
