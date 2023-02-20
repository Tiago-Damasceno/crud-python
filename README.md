# API-CRUD Python 🐍
* Projeto inical de uma API CRUD feito com Python. a proposta é fazer uma API totalmeente funcional e organizada a receber dados feito em MySQL, hospedado em uma local host e por fim podendo ser compartilhada através de um host cedido pela plataforma hostman.

## 📋 Pré-requisitos:
PYTHON 3.11 🐍

FLASK 🌶

HOSTMAN 👩‍🚀

MYSQL 🐬

## 🔧 Instalação

### Criação de um pseudo Banco de Dados em formato Python e importá-lo no API:


ex: ```Motos = [
    {
        'numero': 1,
        'marca': 'Honda',
        'modelo': 'cg125 titan',
        'ano': 1992}```

* A idéia original é importar pseudo banco de dados para o MySQL e permitir que ele continua a ser atualizado.

### Criação da API com FLASK:

*from flask import Flask, make_response, jsonify, request.
from bd  import Motos:*

* Para a criaçção do API éra necessario criar um mecanismo de entrada e de resposta, para resposta usamos ```make_response```.
* depois imortamos nosso "banco de dados" para ser integrado na API.

### hospedando com o HOSTMAN:

* Com o Hostman foi possivel transferir o API de um *Locahost* para um host publico, assim seria possivel versiona-lo ou compartilhar com outros DEVS da equipe. 

## ⚙️ Executando os testes:

* Os testes foram realizados no Proprio Hostman.
 
## 📦 Implantação:

* Para inplantação é necessario gerar um outro host BD no My SQL o que será o porximo passo do porcesso.
* No entanto os testes apenas com o Flask ja são bem satisfatorios

## 🛠️ Construído com:

* FLASK
* HOSTMAN


## 📌 Versão:

v. 0.4.0

## ✒️ Autores:

* Criador: Tiago Damasceno.

## 📄 Licença:

* Licensiado por Tiago Silva Damasceno (devtiago01@gmail.com)

## 🎁 Gratidão:

* Quero agradecer a minha familia que esta me apoiando incondicionalmente no projeto.
* Aos meus colegas de mentoria que sempre me ajudam.
* Aos tutores que são sempre solicitos quando online
* Ao Pedro e ao Henrique meus mentores
* A Deus! sem ele nem aqui eu estaria.
