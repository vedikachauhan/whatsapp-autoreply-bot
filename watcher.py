class Watcher:
    _customers = []

    @property
    def customers(self):
        """getter for property customers
        this property will be used to get the list of customers

        Returns:
            list: the list of customers
        """
        return self._customers

    @customers.setter
    def customers(self, customers):
        """setter for property customers
        this is the setter method to set the name to each object of class customer

        Args:
            customers(list): name of the customer
        """
        self._customers = customers

    def check_new_message(self):
        """method to check new message
        this method will be used to check all the new incoming messages from list of customers

        Return:
            list: the list of customers who have sent new messages
        """
        for customer in self.customers:
            if customer.receive_msg():
                customer.send_msg()
