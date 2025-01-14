# Generated by Django 4.2.6 on 2023-12-08 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CainiaoBased',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.TextField(null=True, verbose_name='')),
                ('CSS3', models.IntegerField(null=True, verbose_name='')),
                ('HTML', models.IntegerField(null=True, verbose_name='')),
                ('Googlemap', models.IntegerField(null=True, verbose_name='')),
                ('Memcached', models.IntegerField(null=True, verbose_name='')),
                ('name', models.IntegerField(null=True, verbose_name='')),
                ('Git', models.IntegerField(null=True, verbose_name='')),
                ('Cpp', models.IntegerField(null=True, verbose_name='')),
                ('jQueryUI', models.IntegerField(null=True, verbose_name='')),
                ('NumPy', models.IntegerField(null=True, verbose_name='')),
                ('Julia', models.IntegerField(null=True, verbose_name='')),
                ('SQL', models.IntegerField(null=True, verbose_name='')),
                ('Scala', models.IntegerField(null=True, verbose_name='')),
                ('HTMLDOM', models.IntegerField(null=True, verbose_name='')),
                ('Rust', models.IntegerField(null=True, verbose_name='')),
                ('Linux', models.IntegerField(null=True, verbose_name='')),
                ('JavaScript', models.IntegerField(null=True, verbose_name='')),
                ('Maven', models.IntegerField(null=True, verbose_name='')),
                ('Bootstrap3', models.IntegerField(null=True, verbose_name='')),
                ('MySQL', models.IntegerField(null=True, verbose_name='')),
                ('MongoDB', models.IntegerField(null=True, verbose_name='')),
                ('Python2x', models.IntegerField(null=True, verbose_name='')),
                ('MVC', models.IntegerField(null=True, verbose_name='')),
                ('FontAwesome', models.IntegerField(null=True, verbose_name='')),
                ('XPath', models.IntegerField(null=True, verbose_name='')),
                ('JSON', models.IntegerField(null=True, verbose_name='')),
                ('Eclipse', models.IntegerField(null=True, verbose_name='')),
                ('PostgreSQL', models.IntegerField(null=True, verbose_name='')),
                ('jQuery', models.IntegerField(null=True, verbose_name='')),
                ('Designpatterns', models.IntegerField(null=True, verbose_name='')),
                ('Nodejs', models.IntegerField(null=True, verbose_name='')),
                ('Chartjs', models.IntegerField(null=True, verbose_name='')),
                ('JSP', models.IntegerField(null=True, verbose_name='')),
                ('Java', models.IntegerField(null=True, verbose_name='')),
                ('Docker', models.IntegerField(null=True, verbose_name='')),
                ('W3C', models.IntegerField(null=True, verbose_name='')),
                ('XLink', models.IntegerField(null=True, verbose_name='')),
                ('Foundation', models.IntegerField(null=True, verbose_name='')),
                ('Echarts', models.IntegerField(null=True, verbose_name='')),
                ('XQuery', models.IntegerField(null=True, verbose_name='')),
                ('Highcharts', models.IntegerField(null=True, verbose_name='')),
                ('Kotlin', models.IntegerField(null=True, verbose_name='')),
                ('Pandas', models.IntegerField(null=True, verbose_name='')),
                ('C', models.IntegerField(null=True, verbose_name='')),
                ('Razor', models.IntegerField(null=True, verbose_name='')),
                ('ASPNET', models.IntegerField(null=True, verbose_name='')),
                ('Scipy', models.IntegerField(null=True, verbose_name='')),
                ('XSLT', models.IntegerField(null=True, verbose_name='')),
                ('WebHosting', models.IntegerField(null=True, verbose_name='')),
                ('SQLite', models.IntegerField(null=True, verbose_name='')),
                ('AppML', models.IntegerField(null=True, verbose_name='')),
                ('Matplotlib', models.IntegerField(null=True, verbose_name='')),
                ('AngularJS', models.IntegerField(null=True, verbose_name='')),
                ('servlet', models.IntegerField(null=True, verbose_name='')),
                ('HTML5', models.IntegerField(null=True, verbose_name='')),
                ('ionic', models.IntegerField(null=True, verbose_name='')),
                ('DTD', models.IntegerField(null=True, verbose_name='')),
                ('PHP', models.IntegerField(null=True, verbose_name='')),
                ('Bootstrap4', models.IntegerField(null=True, verbose_name='')),
                ('SVG', models.IntegerField(null=True, verbose_name='')),
                ('XPointer', models.IntegerField(null=True, verbose_name='')),
                ('BrowserInformation', models.IntegerField(null=True, verbose_name='')),
                ('XSLFO', models.IntegerField(null=True, verbose_name='')),
                ('WebsiteBuilding', models.IntegerField(null=True, verbose_name='')),
                ('jQueryMobile', models.IntegerField(null=True, verbose_name='')),
                ('Vue3', models.IntegerField(null=True, verbose_name='')),
                ('TCPIP', models.IntegerField(null=True, verbose_name='')),
                ('Redis', models.IntegerField(null=True, verbose_name='')),
                ('SOAP', models.IntegerField(null=True, verbose_name='')),
                ('Swift', models.IntegerField(null=True, verbose_name='')),
                ('algorithms', models.IntegerField(null=True, verbose_name='')),
                ('WebService', models.IntegerField(null=True, verbose_name='')),
                ('Perl', models.IntegerField(null=True, verbose_name='')),
                ('ASP', models.IntegerField(null=True, verbose_name='')),
                ('RDF', models.IntegerField(null=True, verbose_name='')),
                ('Svn', models.IntegerField(null=True, verbose_name='')),
                ('VBScript', models.IntegerField(null=True, verbose_name='')),
                ('XML', models.IntegerField(null=True, verbose_name='')),
                ('Vuejs', models.IntegerField(null=True, verbose_name='')),
                ('AJAX', models.IntegerField(null=True, verbose_name='')),
                ('WebPages', models.IntegerField(null=True, verbose_name='')),
                ('Django', models.IntegerField(null=True, verbose_name='')),
                ('TypeScript', models.IntegerField(null=True, verbose_name='')),
                ('c_s', models.IntegerField(null=True, verbose_name='')),
                ('XMLDOM', models.IntegerField(null=True, verbose_name='')),
                ('Bootstrap5', models.IntegerField(null=True, verbose_name='')),
                ('Python', models.IntegerField(null=True, verbose_name='')),
                ('WebsiteQuality', models.IntegerField(null=True, verbose_name='')),
                ('Go', models.IntegerField(null=True, verbose_name='')),
                ('WSDL', models.IntegerField(null=True, verbose_name='')),
                ('CSS', models.IntegerField(null=True, verbose_name='')),
                ('XMLSchema', models.IntegerField(null=True, verbose_name='')),
                ('RSS', models.IntegerField(null=True, verbose_name='')),
                ('HTTP', models.IntegerField(null=True, verbose_name='')),
                ('R', models.IntegerField(null=True, verbose_name='')),
                ('WebForms', models.IntegerField(null=True, verbose_name='')),
                ('Markdown', models.IntegerField(null=True, verbose_name='')),
                ('Lua', models.IntegerField(null=True, verbose_name='')),
                ('AngularJS2', models.IntegerField(null=True, verbose_name='')),
                ('React', models.IntegerField(null=True, verbose_name='')),
                ('Ruby', models.IntegerField(null=True, verbose_name='')),
                ('regular', models.IntegerField(null=True, verbose_name='')),
            ],
            options={
                'verbose_name': 'cainiao_based表管理',
                'verbose_name_plural': 'cainiao_based表管理',
                'db_table': 'cainiao_based',
            },
        ),
        migrations.CreateModel(
            name='Designlist',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField(null=True, verbose_name='')),
                ('name', models.TextField(null=True, verbose_name='')),
                ('url', models.TextField(null=True, verbose_name='')),
                ('design_name', models.TextField(null=True, verbose_name='')),
                ('design_url', models.TextField(null=True, verbose_name='')),
                ('content', models.TextField(null=True, verbose_name='')),
            ],
            options={
                'verbose_name': 'designlist表管理',
                'verbose_name_plural': 'designlist表管理',
                'db_table': 'designlist',
            },
        ),
        migrations.CreateModel(
            name='TitleCount',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField(null=True, verbose_name='')),
                ('count', models.IntegerField(null=True, verbose_name='')),
            ],
            options={
                'verbose_name': 'title_count表管理',
                'verbose_name_plural': 'title_count表管理',
                'db_table': 'title_count',
            },
        ),
        migrations.CreateModel(
            name='UserLike',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.TextField(null=True, verbose_name='')),
                ('like', models.TextField(null=True, verbose_name='')),
            ],
            options={
                'verbose_name': 'user_like表管理',
                'verbose_name_plural': 'user_like表管理',
                'db_table': 'user_like',
            },
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('word', models.TextField(null=True, verbose_name='')),
                ('count', models.IntegerField(null=True, verbose_name='')),
            ],
            options={
                'verbose_name': 'word表管理',
                'verbose_name_plural': 'word表管理',
                'db_table': 'word',
            },
        ),
    ]
