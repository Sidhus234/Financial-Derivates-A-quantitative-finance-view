<h1>Distribution of Random Walks</h1>

We will consider the distribution of <img src="https://render.githubusercontent.com/render/math?math=S_{n}">, the random walk evaluated at time _n_. First, consider the case _n_ = 1. We have:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=S_{1} = X_{1}">
</p>

So, <img src="https://render.githubusercontent.com/render/math?math=S_{1}"> simply has the same distribution as <img src="https://render.githubusercontent.com/render/math?math=X_{1}"> and so

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=Prob \( S_{1} = 1 ) = Prob \( X_{1} = 1 ) = p"><br>
  <img src="https://render.githubusercontent.com/render/math?math=Prob \( S_{1} = -1 ) = Prob \( X_{1} = -1 ) = q = 1 - p"><br>
</p>

Now consider the distribution of <img src="https://render.githubusercontent.com/render/math?math=S_{2}">

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=S_{2} = X_{1} %2B X_{1}">
</p>

<img src="https://render.githubusercontent.com/render/math?math=S_{2}"> may only take the values of +2, 0 , -2. We want to calculate the probabilities of these 3 events.

<ol>
  <li>For the event <img src="https://render.githubusercontent.com/render/math?math=S_{2} = 2"> there is only 1 path the random walk can follow for this to hold: we must have <img src="https://render.githubusercontent.com/render/math?math=X_{1} = 1 and X_{2} = 1">. Hence, <img src="https://render.githubusercontent.com/render/math?math=Prob \( S_{2} =  1 ) = p_{2}"></li>
  <li>Similarly, For the event <img src="https://render.githubusercontent.com/render/math?math=S_{2} = 2"> the <img src="https://render.githubusercontent.com/render/math?math=Prob \( S_{2} = -2 ) = q^{2}"></li>
  <li>For <img src="https://render.githubusercontent.com/render/math?math=S_{2} = 0"> either <img src="https://render.githubusercontent.com/render/math?math=X_{1} = 1 and X_{2} = -1"> or <img src="https://render.githubusercontent.com/render/math?math=X_{1} = -1 and X_{2} = -1">. Hence <img src="https://render.githubusercontent.com/render/math?math=Prob \( S_{2} = 0 ) = pq %2B pq = 2pq"> </li>
</ol>

This is a special case of the binomial distribution: the binomial distribution from 2 trials with a success probability _p_.

<h2>Binomial Distribution</h2>
To continue on to an _n_ step random walk, recall the binomial distribution from elementary probability. We start with Bernoulli random variables <img src="https://render.githubusercontent.com/render/math?math=Y_{1}, Y_{2}, \cdots Y_{n}"> which are independent and each is distributed as the Bernoulli distribution:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=Prob \( Y_{j} = 1 ) = p and Prob \( Y_{j} = 0 ) = q = 1 - p">
</p>

A standard interpretation is that <img src="https://render.githubusercontent.com/render/math?math=Y_{j} = 1"> means "success" on the jth trial, and <img src="https://render.githubusercontent.com/render/math?math=Y_{j} = 0"> is a failure on the jth trial, and _p_ is the "probability of success".

We then defin <img src="https://render.githubusercontent.com/render/math?math=Z_{n}"> to be the total number of successes in _n_ trials. This means:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=Z_{n} = \sum_{j=1}^{n} Y_{j}">
</p>

The distribution of <img src="https://render.githubusercontent.com/render/math?math=Z_{n}"> is studied in elementary probability courses, and is called the __Binomial Distribution__:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=Prob \( Z_{n} = k ) = \frac{n!}{k! \( n - k )!} p^{k} q^{n-k} for k = 0, 1, 2, \cdots n">
</p>

We donote the binomial distribution by bin(k; n, p). Let's consider the special case of n=2:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=Prob \( Z_{2} = 0 ) = bin \( 0 %3B 2, p ) = q^{2}"><br>
  <img src="https://render.githubusercontent.com/render/math?math=Prob \( Z_{2} = 1 ) = bin \( 1 %3B 2, p ) = 2pq"><br>
  <img src="https://render.githubusercontent.com/render/math?math=Prob \( Z_{2} = 2 ) = bin \( 2 %3B 2, p ) = p^{2}"><br>
</p>

These are exactly the probabilities that we calculated for the 2 step random walk. There are many ways to see that this relationship extends to an _n_ step random walk so that the distribution of  <img src="https://render.githubusercontent.com/render/math?math=S_{n}"> is given by binomial probabilities. One approach is:

We relate the Bernoulli random variables <img src="https://render.githubusercontent.com/render/math?math=Y_{j}"> to our jumps <img src="https://render.githubusercontent.com/render/math?math=X_{j}"> by the relation

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=X_{j} = 2 Y_{j} - 1">
</p>

Then <img src="https://render.githubusercontent.com/render/math?math=X_{j} = 1"> when <img src="https://render.githubusercontent.com/render/math?math=Y_{j} = 1"> and <img src="https://render.githubusercontent.com/render/math?math=X_{j} = -1"> when <img src="https://render.githubusercontent.com/render/math?math=Y_{j} = 0">. Also <img src="https://render.githubusercontent.com/render/math?math=X_{j}"> will inherit the same probabilities from <img src="https://render.githubusercontent.com/render/math?math=Y_{j}"> as our assumed model, as well as the independence of successive trials thus replicating our model distribution from <img src="https://render.githubusercontent.com/render/math?math=X_{j}">. Furthermore:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=S_{n} = \sum_{j=1}^{n} X_{j}"><br>
  <img src="https://render.githubusercontent.com/render/math?math== \sum_{j=1}^{n} \( 2 Y_{j} - 1 )"><br>
  <img src="https://render.githubusercontent.com/render/math?math== 2 \sum_{j=1}^{n} Y_{j} - \sum_{j=1}^{n} 1"><br>
  <img src="https://render.githubusercontent.com/render/math?math== 2Z_{n} - n"><br>
</p>

<img src="https://render.githubusercontent.com/render/math?math=S_{n}"> will thus inherit a "shifted" binomial distribution from <img src="https://render.githubusercontent.com/render/math?math=Z_{n}">. For simplicity, we consider the case of even _n = 2m_. In this case, note that <img src="https://render.githubusercontent.com/render/math?math=S_{n}"> can only take as values even integers randing from _-2m to 2m_. Then we will have

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=Prob \( S_{n} = 2l ) = \frac{n!}{ \( m %2B l )! \( m - l )!} p^{m %2B l } q^{m-l} for l = -m, -m %2B 1 \cdots m - 1, m">
</p>
