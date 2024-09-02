document.requestFullscreen();

const die = [4,6,8,10,12,20];
let container =  document.getElementsByClassName('container')[0];
let buttons = [];

function createButtons(){
    let x = 0;
    let y = 0;
    let row = document.getElementsByClassName('buttons-row')[y];

    for(const dice of die){
        let button = document.createElement("button");
        button.setAttribute('class',"button");
        button.setAttribute("id",dice);

        let img = document.createElement("img");
        img.setAttribute('src',"Assets/Sprites/d" + dice + ".png");
        img.setAttribute('alt',"D" + dice);
        let span = document.createElement("span");
        
        button.appendChild(img);
        button.appendChild(span);

        buttons["d" + dice.toString()] = button;
        console.log(buttons["d"+ dice]);
        button.setAttribute("onClick","rollDice(" + dice + ")");
        
        row.appendChild(button);

        x++;
        // TODO: make it so it only makes a new row if x is over 3
        if(x == 3){
            x = 0;
            y++;
            let newRow = document.createElement("div");
            newRow.setAttribute("class","buttons-row");
            container.appendChild(newRow);
            row = document.getElementsByClassName('buttons-row')[y];
        }
    }
}

function rollDice(dice){
    buttons["d" + dice.toString()].children[1].innerHTML = Math.floor(Math.random() * dice);
}

createButtons();