<h2><a href="https://leetcode.com/problems/merge-sorted-array/">88. Merge Sorted Array</a></h2><h3>Easy</h3><hr><div><p>You are given two integer arrays <code>nums1</code> and <code>nums2</code>, sorted in <strong>non-decreasing order</strong>, and two integers <code>m</code> and <code>n</code>, representing the number of elements in <code>nums1</code> and <code>nums2</code> respectively.</p>

<p><strong>Merge</strong> <code>nums1</code> and <code>nums2</code> into a single array sorted in <strong>non-decreasing order</strong>.</p>

<p>The final sorted array should not be returned by the function, but instead be <em>stored inside the array </em><code>nums1</code>. To accommodate this, <code>nums1</code> has a length of <code>m + n</code>, where the first <code>m</code> elements denote the elements that should be merged, and the last <code>n</code> elements are set to <code>0</code> and should be ignored. <code>nums2</code> has a length of <code>n</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre class="" style="position: relative;"><strong>Input:</strong> nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
<strong>Output:</strong> [1,2,2,3,5,6]
<strong>Explanation:</strong> The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [<u>1</u>,<u>2</u>,2,<u>3</u>,5,6] with the underlined elements coming from nums1.
<button class="lazy-felix lazy-felix-download-btn" data-name="ums1 = [1,2,3,0,0,0]"><svg xmlns="http://www.w3.org/2000/svg" class="lazyfelix-icon" width="27" height="25" viewBox="0 0 27 25" fill="none">    <path d="M13.4518 13.0377C11.4186 12.7365 6.4864 16.878 5.39453 21.7726V22.0362C5.48795 24.1899 7.75902 24.9194 10.9292 24.0316C13.0111 23.1639 14.1728 23.1375 16.125 24.0316C17.9698 25.1612 20.41 23.7051 20.643 22.0362C20.3191 18.4517 16.3154 13.1956 13.4518 13.0377Z" fill="#7A7A7A" fill-opacity="0.7"></path>    <ellipse cx="4.85476" cy="11.946" rx="2.97265" ry="4.24369" transform="rotate(-21.5283 4.85476 11.946)" fill="#7A7A7A" fill-opacity="0.7"></ellipse>    <ellipse cx="22.0599" cy="13.5489" rx="2.97265" ry="4.24369" transform="rotate(22.9527 22.0599 13.5489)" fill="#7A7A7A" fill-opacity="0.7"></ellipse>    <ellipse cx="10.1354" cy="5.66514" rx="2.92739" ry="4.7215" transform="rotate(-9.76985 10.1354 5.66514)" fill="#7A7A7A" fill-opacity="0.7"></ellipse>    <ellipse cx="17.552" cy="5.95842" rx="2.92739" ry="4.7215" transform="rotate(14.6303 17.552 5.95842)" fill="#7A7A7A" fill-opacity="0.7"></ellipse>
  </svg></button><button class="lazy-felix lazy-felix-download-btn" data-name="nums1 = [1,2,3,0,0,0]"><svg xmlns="http://www.w3.org/2000/svg" class="lazyfelix-icon" width="27" height="25" viewBox="0 0 27 25" fill="none">    <path d="M13.4518 13.0377C11.4186 12.7365 6.4864 16.878 5.39453 21.7726V22.0362C5.48795 24.1899 7.75902 24.9194 10.9292 24.0316C13.0111 23.1639 14.1728 23.1375 16.125 24.0316C17.9698 25.1612 20.41 23.7051 20.643 22.0362C20.3191 18.4517 16.3154 13.1956 13.4518 13.0377Z" fill="#7A7A7A" fill-opacity="0.7"></path>    <ellipse cx="4.85476" cy="11.946" rx="2.97265" ry="4.24369" transform="rotate(-21.5283 4.85476 11.946)" fill="#7A7A7A" fill-opacity="0.7"></ellipse>    <ellipse cx="22.0599" cy="13.5489" rx="2.97265" ry="4.24369" transform="rotate(22.9527 22.0599 13.5489)" fill="#7A7A7A" fill-opacity="0.7"></ellipse>    <ellipse cx="10.1354" cy="5.66514" rx="2.92739" ry="4.7215" transform="rotate(-9.76985 10.1354 5.66514)" fill="#7A7A7A" fill-opacity="0.7"></ellipse>    <ellipse cx="17.552" cy="5.95842" rx="2.92739" ry="4.7215" transform="rotate(14.6303 17.552 5.95842)" fill="#7A7A7A" fill-opacity="0.7"></ellipse>
  </svg></button><button class="lazy-felix lazy-felix-download-btn" data-name="nums2 = [2,5,6]"><svg xmlns="http://www.w3.org/2000/svg" class="lazyfelix-icon" width="27" height="25" viewBox="0 0 27 25" fill="none">    <path d="M13.4518 13.0377C11.4186 12.7365 6.4864 16.878 5.39453 21.7726V22.0362C5.48795 24.1899 7.75902 24.9194 10.9292 24.0316C13.0111 23.1639 14.1728 23.1375 16.125 24.0316C17.9698 25.1612 20.41 23.7051 20.643 22.0362C20.3191 18.4517 16.3154 13.1956 13.4518 13.0377Z" fill="#7A7A7A" fill-opacity="0.7"></path>    <ellipse cx="4.85476" cy="11.946" rx="2.97265" ry="4.24369" transform="rotate(-21.5283 4.85476 11.946)" fill="#7A7A7A" fill-opacity="0.7"></ellipse>    <ellipse cx="22.0599" cy="13.5489" rx="2.97265" ry="4.24369" transform="rotate(22.9527 22.0599 13.5489)" fill="#7A7A7A" fill-opacity="0.7"></ellipse>    <ellipse cx="10.1354" cy="5.66514" rx="2.92739" ry="4.7215" transform="rotate(-9.76985 10.1354 5.66514)" fill="#7A7A7A" fill-opacity="0.7"></ellipse>    <ellipse cx="17.552" cy="5.95842" rx="2.92739" ry="4.7215" transform="rotate(14.6303 17.552 5.95842)" fill="#7A7A7A" fill-opacity="0.7"></ellipse>
  </svg></button></pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums1 = [1], m = 1, nums2 = [], n = 0
<strong>Output:</strong> [1]
<strong>Explanation:</strong> The arrays we are merging are [1] and [].
The result of the merge is [1].
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> nums1 = [0], m = 0, nums2 = [1], n = 1
<strong>Output:</strong> [1]
<strong>Explanation:</strong> The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>nums1.length == m + n</code></li>
	<li><code>nums2.length == n</code></li>
	<li><code>0 &lt;= m, n &lt;= 200</code></li>
	<li><code>1 &lt;= m + n &lt;= 200</code></li>
	<li><code>-10<sup>9</sup> &lt;= nums1[i], nums2[j] &lt;= 10<sup>9</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up: </strong>Can you come up with an algorithm that runs in <code>O(m + n)</code> time?</p>
</div>