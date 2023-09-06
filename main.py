import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, BloodGroup, Donor, BloodVolume

engine = create_engine('sqlite:///blood_bank.db')
Session = sessionmaker(bind=engine)
session = Session()

@click.group()
def cli():
    pass

@cli.command()
@click.option('--group', prompt='Enter the blood group:', help='Blood group name')
@click.option('--volume', type=int, prompt='Enter the blood volume:', help='Blood volume in milliliters')
@click.option('--date', prompt='Enter the donation date (YYYY-MM-DD):', help='Donation date')
def add_donation(group, volume, date):
    blood_group = BloodGroup(group_name=group)
    session.add(blood_group)

    donor_name = click.prompt('Enter the donor name:')
    donor = Donor(name=donor_name, blood_group=blood_group)
    session.add(donor)

    blood_volume = BloodVolume(blood_group=blood_group, volume=volume)
    session.add(blood_volume)

    session.commit()
    click.echo('Donation added successfully.')

@cli.command()
def list_donations():
    donations = session.query(Donor, BloodGroup, BloodVolume).join(BloodGroup).join(BloodVolume).all()

    for donor, blood_group, blood_volume in donations:
        click.echo(f"Donor: {donor.name}, Blood Group: {blood_group.group_name}, Volume: {blood_volume.volume}")

@cli.command()
@click.argument('donor_id', type=int)
def delete_donation(donor_id):
    donor = session.query(Donor).get(donor_id)
    if donor is not None:
        session.delete(donor)
        session.commit()
        click.echo(f"Donation with ID {donor_id} deleted successfully.")
    else:
        click.echo(f"Donation with ID {donor_id} not found.")

@cli.command()
@click.argument('donor_id', type=int)
@click.option('--new-volume', type=int, prompt='Enter the new blood volume:', help='New blood volume in milliliters')
def update_donation(donor_id, new_volume):
    donor = session.query(Donor).get(donor_id)
    if donor is not None:
        blood_volume = session.query(BloodVolume).filter_by(blood_group=donor.blood_group).first()
        if blood_volume is not None:
            blood_volume.volume = new_volume
            session.commit()
            click.echo(f"Donation with ID {donor_id} updated successfully.")
        else:
            click.echo(f"Donation with ID {donor_id} does not have a corresponding blood volume.")
    else:
        click.echo(f"Donation with ID {donor_id} not found.")

@cli.command()
def create_table():
    Base.metadata.create_all(engine)
    click.echo("Table created successfully.")

if __name__ == '__main__':
    cli()