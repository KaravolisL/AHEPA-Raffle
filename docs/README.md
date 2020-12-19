# Help Documentation

## Downloading the Application

Visit the following link to download a zipped folder containing the application:

![Download Link](https://github.com/KaravolisL/AHEPA-Raffle/releases)

## Launching the Program

To launch the program, double-click Main.exe in the distributed src folder. It may take a minute or two to launch.

![Launching the Program](https://github.com/KaravolisL/AHEPA-Raffle/raw/master/docs/screenshots/LaunchingProgram.PNG)

## Basic Layout
The following is what you should see when the program initially starts.

![Base Screenshot](https://github.com/KaravolisL/AHEPA-Raffle/raw/master/docs/screenshots/Base.PNG)

In the top right, you have a menu bar that can be used to access a variety of features. Below that is the header. It displays how many tickets are remaining, how many tickets have been drawn, and the last ticket that had been drawn. Below this is the main table that holds the 225 tickets.

## Setting up the Raffle

### Tickets

The first thing you'll probably want to do is add the names to each of the tickets. This can be done in one of two ways. First, hovering over the Edit menu and clicking Edit Ticket will display the following window:

![Edit Ticket Window](https://github.com/KaravolisL/AHEPA-Raffle/raw/master/docs/screenshots/EditTicketWindow.PNG)

In here, you can type a ticket number and the name and hit the change name button. You should be able to see the new ticket name now. Alternatively, you can import the ticket names from a text file. The following file format is supported:

![Ticket Names File Format](https://github.com/KaravolisL/AHEPA-Raffle/raw/master/docs/screenshots/TicketNamesFileFormat.PNG)

Once you have the correctly formatted file, navigate to the import ticket menu option located under the file menu. You will be prompted to select the text file. After selecting, the names will be added to the tickets.

### Prizes

Next, you might want to add prizes. Again, this can be done one of two ways. Prizes can be entered one by one by navigating to the Edit Prize window under the Edit menu bar option. This shows the following window:

![Edit Prize Window](https://github.com/KaravolisL/AHEPA-Raffle/raw/master/docs/screenshots/EditPrizeWindow.PNG)

Here, you can select the number for the prize and the description that will be printed on the alert. The alerts will show after the ticket before the prize number has been drawn. Alternatively, you can also import a text file formatted in the following way:

![Prizes File Format](https://github.com/KaravolisL/AHEPA-Raffle/raw/master/docs/screenshots/PrizeFileFormat.PNG)

Similarly, navigate to the Import Prizes option under the File menu. This pulls up a similar window to that of the Import Tickets window. After selecting your file, the prizes will be imported into the program.

### Verification

Both the ticket names and the prizes can be verified by selecting both View Ticket Names and View Prizes under the View menu. The following windows will be displayed:

![View Ticket Names](https://github.com/KaravolisL/AHEPA-Raffle/raw/master/docs/screenshots/ViewTicketNames.PNG)

![View Prizes](https://github.com/KaravolisL/AHEPA-Raffle/raw/master/docs/screenshots/ViewPrizes.PNG)

### Editing the Background Color

The background colors of both the main table and the header can be changed by the user. Under the Edit menu, click Change Background Color. From here, you can click each current color to select a new one.

![Change Background Color](https://github.com/KaravolisL/AHEPA-Raffle/raw/master/docs/screenshots/ChangeBackgroundColor.PNG)

### Prize Alerts

Prize alerts will appear when the ticket prior to the ticket with a prize has been drawn. For example, if there is a prize for ticket 25, a prize alert will appear when the 24th ticket is drawn. These alerts will display the prize's description for a set amount of time. Note that the alerts can also be closed early by clicking on them or pressing enter. The alert boxes can also be customized more thoroughly. Specifically, you can change the background color, the font size, and the duration for which they remain on the screen. The customization window is located under the Edit menu and the Edit Prize Alert option.

![Edit Prize Alert](https://github.com/KaravolisL/AHEPA-Raffle/raw/master/docs/screenshots/EditPrizeAlert.PNG)

## Operating the Program

### Full Screen

Full screen mode can be used to hide the window border and the menu bar. To enter full screen, click Full Screen located under the View menu. You can exit full screen mode by pressing the escape button.

### Removing Tickets

You can remove a ticket simply by clicking any of the 225 tickets. The ticket will disappear, and the header will be updated with the new information.

### Undo

You might make a mistake and have to replace a ticket that was drawn. To do this, simply click the right most cell of the header labeled Last Ticket Drawn. This will undo the last action that was taken by making a ticket visible and updating the header accordingly.

![Undo Button](https://github.com/KaravolisL/AHEPA-Raffle/raw/master/docs/screenshots/UndoButton.png)

### Control Panel

Alternatively, you can use the control panel view on a separate display to operate the application. From this view, you can view the information in the header, remove and replace tickets, and see the next prize to be won.

![Control Panel](https://github.com/KaravolisL/AHEPA-Raffle/raw/master/docs/screenshots/ControlPanel.png)

### Restarting the Raffle

All tickets can be replaced by hitting the Restart Raffle option under the File menu. This will cause all progress to be lost!

## Additional Features

+ Closing the program will cause the current progress to be automatically saved. When the program is opened again, the progress will be restored.