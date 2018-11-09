class AuthenticateView:
    """ Class to authenticate views."""

    def authenticate_parcel_order(self, pick_up, destination):
        """ Method to authenticate parcel order."""

        if (pick_up.isspace() or not pick_up.isalpha()) and destination.isspace() or not destination.isalpha():
            return "Location should only be a string."
