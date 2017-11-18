
class Status:
    just_started = 0

    @staticmethod
    def create_status(action, parameter):
        return "{} {}".format(action, parameter)

    @staticmethod
    def create_choosed_status(parameter):
        return "{} {}".format("choosed", parameter)

    @staticmethod
    def was_choosed_smth(status):
        return status.split(' ')[0] == 'choosed'

    @staticmethod
    def was_sent_geo(status):
        return status.split(' ')[0] == 'geo'

    @staticmethod
    def choosed_to_geo(status):
        return 'geo ' + status.split(' ')[1]

    @staticmethod
    def get_id_of_choosen(status):
        return status.split(' ')[1]

    @staticmethod
    def is_adding_a_place(status):
        return status.split(' ')[0] == 'add_place'
