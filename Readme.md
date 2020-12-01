This simple cli interface will help you organise your favourite webpages in your system through command line.<br> 
Presently most of things work in linux. The project is in developing mode as there are lot of improvements that can be done.<br>
So, if there are any suggestions please open a issue.

*Installation:* 
1. clone the repository
2. go in the repo directory
3. run pip or pip3 install -e ./(Installing in editable mode)
4. Now you can use it as KeepBlog

*You can remove it easily thorugh pip3 or pip uninstall KeepBlog*

<b>Example usage:</b><br>
KeepBlog
<pre>
Usage: KeepBlog [OPTIONS] COMMAND [ARGS]...

  Simple CLI for saving your favourite webpages like blogs  under different
  topics and then seeing them whenever you wish

Options:
  --help  Show this message and exit.

Commands:
  addblog   Add your favourite Page
  open      Open the webpage in your browser
  remove    If you run without any options this will delete all saved
            pages,...
  seepages  See all saved pages of a topic
</pre>

KeepBlog seepages
<pre>
There are 0 topics
</pre>

KeepBlog addblog SegmentTrees SegmentTreesProblems https://codeforces.com/blog/entry/22616 <br>
<pre></pre>
KeepBlog seepages
<pre>
There are 1 topics
SegmentTrees
Input a topic to see all the pages within it: SegmentTrees
Name-> SegmentTreesProblems, Link-> https://codeforces.com/blog/entry/22616
</pre>

KeepBlog open SegmentTreesProblems
<pre>Opening in your browser</pre>
and then it opens in a new tab in your browser.

KeepBlog remove
<pre>
Password: 
Repeat for confirmation: 
</pre>

KeepBlog seepages
<pre>
There are 0 topics
</pre>

You can use command remove to remove any particular topic or page also. <br>
Check with KeepBlog remove --help.