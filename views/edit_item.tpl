<html>
<body>
Edit the game
<hr/>
<form action="/edit/{{id}}" method="post">
  <p>Edit Item:<input name="name" value="{{name}}"/></p>
  <p><button type="submit">Submit</button></p>
</form>
<hr/>
<a href="/list">Cancel</a>
</body>
</html>