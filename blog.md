---
layout: default
---

<ul class="posts">
  {% for post in site.categories.blog %}
    <li>{{ post.date | date_to_string }} » <a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>
