from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from pathlib import Path

app = Flask(__name__)
app.config["SECRET_KEY"] = "troque-esta-chave-em-producao"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tarefas.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(120), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    concluida = db.Column(db.Boolean, default=False, nullable=False)
    criada_em = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)


@app.route("/")
def index():
    tarefas = Tarefa.query.order_by(Tarefa.criada_em.desc()).all()
    return render_template("index.html", tarefas=tarefas)


@app.route("/criar", methods=["POST"])
def criar():
    titulo = request.form.get("titulo", "").strip()
    descricao = request.form.get("descricao", "").strip()

    if not titulo:
        flash("O título é obrigatório.", "erro")
        return redirect(url_for("index"))

    tarefa = Tarefa(titulo=titulo, descricao=descricao)
    db.session.add(tarefa)
    db.session.commit()
    flash("Tarefa cadastrada com sucesso!", "sucesso")
    return redirect(url_for("index"))


@app.route("/editar/<int:tarefa_id>", methods=["GET", "POST"])
def editar(tarefa_id):
    tarefa = Tarefa.query.get_or_404(tarefa_id)

    if request.method == "POST":
        titulo = request.form.get("titulo", "").strip()
        if not titulo:
            flash("O título é obrigatório.", "erro")
            return render_template("editar.html", tarefa=tarefa)

        tarefa.titulo = titulo
        tarefa.descricao = request.form.get("descricao", "").strip()
        db.session.commit()
        flash("Tarefa atualizada com sucesso!", "sucesso")
        return redirect(url_for("index"))

    return render_template("editar.html", tarefa=tarefa)


@app.route("/alternar/<int:tarefa_id>", methods=["POST"])
def alternar(tarefa_id):
    tarefa = Tarefa.query.get_or_404(tarefa_id)
    tarefa.concluida = not tarefa.concluida
    db.session.commit()
    flash("Status atualizado.", "sucesso")
    return redirect(url_for("index"))


@app.route("/excluir/<int:tarefa_id>", methods=["POST"])
def excluir(tarefa_id):
    tarefa = Tarefa.query.get_or_404(tarefa_id)
    db.session.delete(tarefa)
    db.session.commit()
    flash("Tarefa excluída.", "sucesso")
    return redirect(url_for("index"))


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
