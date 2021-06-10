from flask_wtf import form
import os
from werkzeug.utils import secure_filename
from travel.models import Destination
from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Destination, Comment
from .forms import DestinationForm, CommentForm
from. import db

bp = Blueprint('destination', __name__, url_prefix='/destinations')

def check_upload_file(form):
    fp = form.image.data
    filename = fp.filename
    BASE_PATH = os.path.dirname(__file__)
    upload = os.path.join(BASE_PATH, 'static/image', secure_filename(filename))
    db_upload_path = '/static/image/' + secure_filename(filename)
    fp.save(upload)
    return (db_upload_path)

@bp.route('/<id>')
def show (id):
    destination = Destination.query.filter_by(id=id).first()
    comment_form = CommentForm()
    return render_template('destinations/show.html', destination=destination, cform=comment_form)

@bp.route('/create', methods=['GET', 'POST'])
def create():
  print(f'Method Type: {request.method}')
  destination_form = DestinationForm()
  
  #if request method is post
  if destination_form.validate_on_submit():
    db_file_path = check_upload_file(destination_form)
    destination = Destination (
      name=destination_form.name.data,
      description = destination_form.description.data,
      image=db_file_path,
      currency=destination_form.currency.data
    )
    db.session.add(destination)
    db.session.commit()
    destination.id
    flash(f'Successfully created a {destination_form.name.data}', 'success')
    return redirect(url_for('destination.show', id=destination.id))

  return render_template('destinations/create.html', form=destination_form)

@bp.route('/<id>/comment', methods=['GET','POST'])
def comment(id):
  comment_form = CommentForm()
  destination = Destination.query.filter_by(id=id).first()
  if comment_form.validate_on_submit():
    comment = Comment(
      text = comment_form.text.data,
      destination=destination
    )
    db.session.add(comment)
    db.session.commit()

    flash('Comment created!', 'success')
    flash(f'Comment text:\n{comment_form.text.data}')
  else:
    flash('Issue posting comment', 'danger')

  return redirect(url_for('destination.show', id=id))

