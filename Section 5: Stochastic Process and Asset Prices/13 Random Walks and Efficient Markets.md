<h1>Random Walks and Efficient Markets</h1>

<h2>Criticisms</h2>
<li>A Radnom walk is as likely to take negative values as positive ones. Asset prices, at least the cas products, do not take negative values.</li>
<li>A more subtle, but related problem, is that the jump size is fixed and insensitive to the price level. The jump is <img src="https://render.githubusercontent.com/render/math?math=X_{j} = \pm 1"> regardless of the price level. For example, if we chose to use the standard random walk we have introduced as a model for a stock price, then the jump in the stock at every time step is up or down by $1 whether the stock is trading at $100 or $2. A jump of $1 implies a 1% return if the stock is trading at $100 and 1 50% return if it is at $2. Investors are primarily concerned with returns, regardless of the absolute levels of prices. So a more reasonable model would be one where the stock could jump by either +$2 or -$2 if the stock price is $20 and +20 or -$20 if the stock price is $200. The random walk model we discussed cannot do this.</li>

<h2>Some Features of Random Walks</h2>
<li>The key property of the random walk process: every jump at each time step is completely independent of the entire history of the process that precedes it. Therefore any information derived from that history is useless for predicting what the next jump will be. This corresponds to a fudamental idea of financial economics: the __Efficient Market Hypothesis (EMH)__.</li>
<li>The random walk model is a very strong and restrictive case of the EMH. Probabilistic independence is not required: only that the information available on any day cannot be used to systematically make a profitable prediction of what the price will be the next day.</li>

<h2>Summary</h2>
EMH is considered desirable to treat it as abase case, to which modifications can be made to account for the complexities of real world markets. And amongst different model implementations of EMH, the random walk model may be considered a base case that is simple to work with and understand. Therefore, to develop a model for asset prices, we will seek out adaptations and extensions of the basic random walk model, that remedy the shortcomings we have noted in this lecture, but still retain aspects of market efficiency.

<h2>Efficient Market Hypothesis</h2>
It is the idea that all available information, relevant to a given asset's price, is taken into account by the price at any time. Thus, the EMH implies , in particular, that the history of the price contains no infromation that can be used to predict the next move in the price. The random walk model is one way to implement this. EMH itself is a controversial idea. It has some theoretical and empirical support. But there is also empirical evidence that contradicts it. Nevertheless, the EMH has broad support in financial economics as a fundamentally correct idea, even though it may not be quantitativewly accurate at a detailed level. 
