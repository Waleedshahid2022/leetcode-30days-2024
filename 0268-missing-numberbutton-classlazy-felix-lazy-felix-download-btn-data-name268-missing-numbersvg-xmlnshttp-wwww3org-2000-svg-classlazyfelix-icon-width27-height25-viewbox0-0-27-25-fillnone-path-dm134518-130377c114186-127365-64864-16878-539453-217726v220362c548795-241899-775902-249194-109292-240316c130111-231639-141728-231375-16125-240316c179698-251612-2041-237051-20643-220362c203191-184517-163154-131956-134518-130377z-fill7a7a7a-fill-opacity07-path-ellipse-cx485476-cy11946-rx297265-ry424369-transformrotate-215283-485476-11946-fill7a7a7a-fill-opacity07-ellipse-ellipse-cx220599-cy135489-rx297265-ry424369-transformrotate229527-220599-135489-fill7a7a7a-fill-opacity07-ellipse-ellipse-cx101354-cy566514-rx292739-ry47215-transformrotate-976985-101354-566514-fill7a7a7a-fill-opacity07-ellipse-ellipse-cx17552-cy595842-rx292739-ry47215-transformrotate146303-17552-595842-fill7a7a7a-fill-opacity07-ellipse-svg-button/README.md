<h2><a href="https://leetcode.com/problems/missing-number/">268. Missing Number<button class="lazy-felix lazy-felix-download-btn" data-name="268. Missing Number"><svg xmlns="http://www.w3.org/2000/svg" class="lazyfelix-icon" width="27" height="25" viewBox="0 0 27 25" fill="none">    <path d="M13.4518 13.0377C11.4186 12.7365 6.4864 16.878 5.39453 21.7726V22.0362C5.48795 24.1899 7.75902 24.9194 10.9292 24.0316C13.0111 23.1639 14.1728 23.1375 16.125 24.0316C17.9698 25.1612 20.41 23.7051 20.643 22.0362C20.3191 18.4517 16.3154 13.1956 13.4518 13.0377Z" fill="#7A7A7A" fill-opacity="0.7"></path>    <ellipse cx="4.85476" cy="11.946" rx="2.97265" ry="4.24369" transform="rotate(-21.5283 4.85476 11.946)" fill="#7A7A7A" fill-opacity="0.7"></ellipse>    <ellipse cx="22.0599" cy="13.5489" rx="2.97265" ry="4.24369" transform="rotate(22.9527 22.0599 13.5489)" fill="#7A7A7A" fill-opacity="0.7"></ellipse>    <ellipse cx="10.1354" cy="5.66514" rx="2.92739" ry="4.7215" transform="rotate(-9.76985 10.1354 5.66514)" fill="#7A7A7A" fill-opacity="0.7"></ellipse>    <ellipse cx="17.552" cy="5.95842" rx="2.92739" ry="4.7215" transform="rotate(14.6303 17.552 5.95842)" fill="#7A7A7A" fill-opacity="0.7"></ellipse>
  </svg></button></a></h2><h3>Easy</h3><hr><div><p class="" style="position: relative;">Given an array <code>nums</code> containing <code>n</code> distinct numbers in the range <code>[0, n]</code>, return <em>the only number in the range that is missing from the array.</em><button class="lazy-felix lazy-felix-download-btn" data-name=" distinct numbers in the range"><svg xmlns="http://www.w3.org/2000/svg" class="lazyfelix-icon" width="27" height="25" viewBox="0 0 27 25" fill="none">    <path d="M13.4518 13.0377C11.4186 12.7365 6.4864 16.878 5.39453 21.7726V22.0362C5.48795 24.1899 7.75902 24.9194 10.9292 24.0316C13.0111 23.1639 14.1728 23.1375 16.125 24.0316C17.9698 25.1612 20.41 23.7051 20.643 22.0362C20.3191 18.4517 16.3154 13.1956 13.4518 13.0377Z" fill="#7A7A7A" fill-opacity="0.7"></path>    <ellipse cx="4.85476" cy="11.946" rx="2.97265" ry="4.24369" transform="rotate(-21.5283 4.85476 11.946)" fill="#7A7A7A" fill-opacity="0.7"></ellipse>    <ellipse cx="22.0599" cy="13.5489" rx="2.97265" ry="4.24369" transform="rotate(22.9527 22.0599 13.5489)" fill="#7A7A7A" fill-opacity="0.7"></ellipse>    <ellipse cx="10.1354" cy="5.66514" rx="2.92739" ry="4.7215" transform="rotate(-9.76985 10.1354 5.66514)" fill="#7A7A7A" fill-opacity="0.7"></ellipse>    <ellipse cx="17.552" cy="5.95842" rx="2.92739" ry="4.7215" transform="rotate(14.6303 17.552 5.95842)" fill="#7A7A7A" fill-opacity="0.7"></ellipse>
  </svg></button></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre class="" style="position: relative;"><strong>Input:</strong> nums = [3,0,1]
<strong>Output:</strong> 2
<strong>Explanation:</strong> n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
<button class="lazy-felix lazy-felix-download-btn" data-name="3,0,1]
"><svg xmlns="http://www.w3.org/2000/svg" class="lazyfelix-icon" width="27" height="25" viewBox="0 0 27 25" fill="none">    <path d="M13.4518 13.0377C11.4186 12.7365 6.4864 16.878 5.39453 21.7726V22.0362C5.48795 24.1899 7.75902 24.9194 10.9292 24.0316C13.0111 23.1639 14.1728 23.1375 16.125 24.0316C17.9698 25.1612 20.41 23.7051 20.643 22.0362C20.3191 18.4517 16.3154 13.1956 13.4518 13.0377Z" fill="#7A7A7A" fill-opacity="0.7"></path>    <ellipse cx="4.85476" cy="11.946" rx="2.97265" ry="4.24369" transform="rotate(-21.5283 4.85476 11.946)" fill="#7A7A7A" fill-opacity="0.7"></ellipse>    <ellipse cx="22.0599" cy="13.5489" rx="2.97265" ry="4.24369" transform="rotate(22.9527 22.0599 13.5489)" fill="#7A7A7A" fill-opacity="0.7"></ellipse>    <ellipse cx="10.1354" cy="5.66514" rx="2.92739" ry="4.7215" transform="rotate(-9.76985 10.1354 5.66514)" fill="#7A7A7A" fill-opacity="0.7"></ellipse>    <ellipse cx="17.552" cy="5.95842" rx="2.92739" ry="4.7215" transform="rotate(14.6303 17.552 5.95842)" fill="#7A7A7A" fill-opacity="0.7"></ellipse>
  </svg></button><button class="lazy-felix lazy-felix-download-btn" data-name="[3,0,1]"><svg xmlns="http://www.w3.org/2000/svg" class="lazyfelix-icon" width="27" height="25" viewBox="0 0 27 25" fill="none">    <path d="M13.4518 13.0377C11.4186 12.7365 6.4864 16.878 5.39453 21.7726V22.0362C5.48795 24.1899 7.75902 24.9194 10.9292 24.0316C13.0111 23.1639 14.1728 23.1375 16.125 24.0316C17.9698 25.1612 20.41 23.7051 20.643 22.0362C20.3191 18.4517 16.3154 13.1956 13.4518 13.0377Z" fill="#7A7A7A" fill-opacity="0.7"></path>    <ellipse cx="4.85476" cy="11.946" rx="2.97265" ry="4.24369" transform="rotate(-21.5283 4.85476 11.946)" fill="#7A7A7A" fill-opacity="0.7"></ellipse>    <ellipse cx="22.0599" cy="13.5489" rx="2.97265" ry="4.24369" transform="rotate(22.9527 22.0599 13.5489)" fill="#7A7A7A" fill-opacity="0.7"></ellipse>    <ellipse cx="10.1354" cy="5.66514" rx="2.92739" ry="4.7215" transform="rotate(-9.76985 10.1354 5.66514)" fill="#7A7A7A" fill-opacity="0.7"></ellipse>    <ellipse cx="17.552" cy="5.95842" rx="2.92739" ry="4.7215" transform="rotate(14.6303 17.552 5.95842)" fill="#7A7A7A" fill-opacity="0.7"></ellipse>
  </svg></button></pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [0,1]
<strong>Output:</strong> 2
<strong>Explanation:</strong> n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre class="" style="position: relative;"><strong>Input:</strong> nums = [9,6,4,2,3,5,7,0,1]
<strong>Output:</strong> 8
<strong>Explanation:</strong> n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
<button class="lazy-felix lazy-felix-download-btn" data-name="[9,6,4,2,3,5,7,0,1]"><svg xmlns="http://www.w3.org/2000/svg" class="lazyfelix-icon" width="27" height="25" viewBox="0 0 27 25" fill="none">    <path d="M13.4518 13.0377C11.4186 12.7365 6.4864 16.878 5.39453 21.7726V22.0362C5.48795 24.1899 7.75902 24.9194 10.9292 24.0316C13.0111 23.1639 14.1728 23.1375 16.125 24.0316C17.9698 25.1612 20.41 23.7051 20.643 22.0362C20.3191 18.4517 16.3154 13.1956 13.4518 13.0377Z" fill="#7A7A7A" fill-opacity="0.7"></path>    <ellipse cx="4.85476" cy="11.946" rx="2.97265" ry="4.24369" transform="rotate(-21.5283 4.85476 11.946)" fill="#7A7A7A" fill-opacity="0.7"></ellipse>    <ellipse cx="22.0599" cy="13.5489" rx="2.97265" ry="4.24369" transform="rotate(22.9527 22.0599 13.5489)" fill="#7A7A7A" fill-opacity="0.7"></ellipse>    <ellipse cx="10.1354" cy="5.66514" rx="2.92739" ry="4.7215" transform="rotate(-9.76985 10.1354 5.66514)" fill="#7A7A7A" fill-opacity="0.7"></ellipse>    <ellipse cx="17.552" cy="5.95842" rx="2.92739" ry="4.7215" transform="rotate(14.6303 17.552 5.95842)" fill="#7A7A7A" fill-opacity="0.7"></ellipse>
  </svg></button></pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= n</code></li>
	<li>All the numbers of <code>nums</code> are <strong>unique</strong>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you implement a solution using only <code>O(1)</code> extra space complexity and <code>O(n)</code> runtime complexity?</p>
</div>