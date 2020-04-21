---
layout: default
title: Resources
description: Workshop resources
---

- [Python v3.7 documentation](https://docs.python.org/3.7/)
- [pygame documentation](https://www.pygame.org/docs/)
- [repl.it Python](https://repl.it/languages/python3)
- [repl.it PyGame](https://repl.it/languages/pygame)
- [Invent with Python's 'Making Games with Python and Pygame'](https://inventwithpython.com/pygame/)
- [Thonny](https://thonny.org/)

# Example Code

<ul class="posts">
  {% assign posts_by_author = site.categories.examples | sort: "author" %}
  {% for post in posts_by_author %}
    <li>{{post.author}} » <a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>

