## API com Python, Flask e SQLAlchemy

### Dependências a serem instaladas
<p>pip install Flask</p>
<p>pip install Flask-RESTful</p>
<p>pip install flask-jwt-extended</p>

### Banco de dados sqlite3
<p>Não há necessidade de fazer download do banco, o mesmo é criado na execução da aplicação.</p>

### Comando para rodar a aplicação
flask run

### Endpoints da aplicação
<p>Para realizar o login, requisição do tipo POST.
Retorna o token Bearer
http://127.0.0.1:5000/login</p>


<p>Para Adicionar/Consultar/Alterar/Deletar um book.
É necessário enviar o book_id e adicionar o Authorization Bearer no header e enviar o token junto com a requisição.
Para cadastrar/alterar também é necessário enviar um objeto contendo o book_name, book_author, book_edition.
http://127.0.0.1:5000/book/<book_id></p>