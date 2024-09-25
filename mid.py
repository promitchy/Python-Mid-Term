class Star_movie():
    hall_list=[]
    def __init__(self):
        pass
    def _entry_hall(self,hall):
        self.hall_list.append(hall)

class Hall(Star_movie):
    def __init__(self,rows,cols,hall_no):
        self.__seats={}
        self.__show_list=[]
        self.__rows=rows
        self.__cols=cols
        self.__hall_no=hall_no
        super().__init__()
        self._entry_hall(self)
    
    def entry_show(self,id,movie_name,time):
        self.id=id
        self.movie_name=movie_name
        self.time=time
        show_information=(id,movie_name,time)
        self.__show_list.append(show_information)
        seat_list=[[0 for i in range (0,self.__cols)] for j in range (0,self.__rows)]
        self.__seats[id]=seat_list

    def book_seats(self,showId,TupleList):
        if showId not in self.__seats:
            print(f'{showId} is not a valid id,try again and input a valid id')
        else:
            for (row,col) in TupleList:
                if 0<=row<self.__rows and 0<=col<self.__cols:
                    if self.__seats[id][row][col]=='confirmed':
                        print(f'Id={showId}->Seat={row},{col} is already booked,try again and input another seat number')
                    else:
                        self.__seats[id][row][col]='confirmed'
                        print(f'Id={showId}->Seat={row},{col} is successfully booked for the show')
                else:
                    print(f'invlid seat number ,try again and input a valid seat number')
    
    def view_show_list(self):
        if self.__show_list.__len__()==0:
            print("No show is running")
        else:
            for show in self.__show_list:
                print(f'Show Id: {show[0]},Movie Name: {show[1]}, Time: {show[2]} -> running this show')
    
    def view_available_seats(self,ShowId):
        if id not in self.__seats:
            print('Sorry ,Id is not found')
            return
        availavle_seat=[]
        for row in range(self.__rows):
            for col in range(self.__cols):
                if self.__seats[id][row][col]== 0:
                    temp=(row,col)
                    print(temp)
                    availavle_seat.append(temp)
        if availavle_seat:
            print(f'available show for this id : {ShowId}')
            for seat in availavle_seat:
                print(f'seats ->{seat[0]}, {seat[1]}')
        else:
            print(f'No available show for this id : {ShowId}')


movie=Hall(8,8,100)
movie.entry_show(1,'Hulk','25/01/2021')
movie.entry_show(2,'Iron Man','03/08/2012')
movie.entry_show(3,'Captain America','15/05/2024')
movie.entry_show(4,'Spider Man','30/12/2024')

running=True
while running:
    print('1->View Show List')
    print('2->View available Seat')
    print('3->Book a seat')
    print('4->Finish')

    No=int(input("Enter Your Choice :"))
    if No==1:
        movie.view_show_list()
    elif No==2:
        id=int(input("Please enter your id to see available seat :"))
        movie.view_available_seats(id)
    elif No==3:
        Ticket=int(input("Enter No of Ticket: "))
        while Ticket!= 0:
            id=int(input("Enter Your Id: "))
            row=int(input('Enter Row: '))
            col=int(input('Enter Col: '))
            TupleList=[(row,col)]
            movie.book_seats(id ,TupleList)
            Ticket-=1 
    elif No==4:
        print("Finishing work")
        running=False
