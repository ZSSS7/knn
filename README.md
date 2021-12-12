# k-近邻
简单实现一下k近邻算法的原理

k近邻基本原理是：如果一个样本在特征空间中的k个最相似(即特征空间中最邻近)的样本中的大多数属于某一个类别，则该样本也属于这个类别。

简单来说就是，如果有两类样本进行分类，输入一个新的样本，计算新样本与原来样本之间的距离，与它最接近的K个样本中出现最多的类别，就是新样本的类别。
第一类如下图所示：
![Figure_1](https://user-images.githubusercontent.com/68314193/145700492-6e4fde5a-96a5-42d5-a39f-62acf3f8a190.png)

第二类如下图所示：

![Figure_2](https://user-images.githubusercontent.com/68314193/145700496-e76180aa-09da-479e-ab81-c460d765eadf.png)

输入一个新样本（黄色），计算与新样本距离最近的K个点

![Figure_3](https://user-images.githubusercontent.com/68314193/145700521-ba0e1374-abcd-4959-bf54-10067de2a510.png)

如上图所示，该样本属于X类。
