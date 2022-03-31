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




















<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=">
</p>


<img src="../Images/S9_working_Capital_days.png" alt="Working Capital Days"/>
