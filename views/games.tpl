<html>
<body>
<h2>GAMES</h2>
<hr/>
<table>
% for item in games:
  <tr>
    <td>{{str(item['desc'])}}</td>
    <td><a href="/edit/{{str(item['id'])}}">edit</a></td>
    <td><a href="/delete/{{str(item['id'])}}">delete</a></td>
  </tr>
% end
</table>
<hr/>
<form action="/add" method="post">
  <p>Add new item: <input name="name"/></p>
  <p><button type="submit">Submit</button>
</form>
</body>
</html>


