cReAtE table MyTable  (  id    int     primary key,Name varchar(  50 ),   created_at   datetime default current_timestamp   );
insert  into MyTable(id,Name ) values(1,'John Doe');
iNsErT inTo MyTable (id,Name)   vAlUeS  (2,'Jane Smith' );SELecT   Id,Name,  created_at    FROM     MyTable   WHere     name='John Doe'   or    NAME='Jane Smith'    order     BY   created_at desc;uPdAtE  MyTable SeT Name='John D', created_at=current_timestamp    wHeRe id=1;
DeLeTe from MyTable where Id=2;