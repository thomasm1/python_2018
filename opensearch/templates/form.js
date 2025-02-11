import { $$, getConvertCSV, preProcessCSV, csvToJSO } from "./shared.js";
//DATA SOURCE
// const dataFromRestApi = "http://localhost:8080/data RestApi delivering from DB
// const dataJsonUrl = "../data/dbArray.json";
// const dataJsonUrl = "http://127.0.0.1:3000/data 

const dataCsv = "../data/data9006.csv";

////// I. /// page objects //////

///// show/hide based on radio
const formObj = $$("form");   // .form
const scrollMax = "240"; // scrollwindow 
// input dropdown
let opt1 = $$("#opt1");
let opt2 = $$("#opt2");

// show/hide opt1 VS opt2
let divOpt1 = $$("#divOpt1"); // input region hidden or shown
let divOpt2 = $$("#divOpt2");

const filterOpt1 = $$("#filterBoxOpt1"); //input field
const filterOpt2 =  $$("#filterBoxOpt2");
const matchList = $$("#match-list"); // output html region for filtermatches

const searchBox = $$(".search-box input"); // == filterOpt1
const opt1Checked = $$("opt1Checked");
const opt1DivChecked = $$("#opt1DivChecked");

///// multiselect
const selectAny = $$("#selectAny");
const select1 = $$("#select1");
const select2 = $$("#select2");
const selectBoth = $$("#selectBoth");

const selectTypes = $$(".select-types")

/////// II. ///Methods

//func 1: index.js obtain value clicked assign to var
optionClicked = (opt1Clicked, opt2Clicked) => {
    filterOpt1.value = opt1Clicked;
    filterOpt2.value = opt2Clicked;
    //close after option clicked
    matchList.style.visibility = "hidden"
};

//func 2: input filter gets data from API or local file
//search docList.json and filter
let matches = []
const filterData = async(firstLetters) => {
    //access CSV
    let dataFromCsv = await getConvertCSV(dataCsv);
    console.log("getConvert", dataFromCsv) 

    //match to current text input --keyup
    matches = await dataFromCsv.filter((data) => {
        let regexOption; // for breaking up query by spaces: , regex2, regex3, regex4;
        let num, text;

        regexOption= new RegExp(`^${firstLetters}`, "gi")
        text = data.headers[0].match(regexOption)

        if(firstLetters.length >0) {
            return text;
        } else if(firstLetters.length===0) {
            matches = [];
            matchList.innerHTML = "";
        }

    });
    outputHtml(matches);
};

//func 3: show filtered data in HTML
const outputHtml = (matchingDataArray) => {
    if(matchingDataArray.length > 0) {
        matchList.style.visibility = "visible";
        const html = matchingDataArray
            .map(
                (match) => `
                <!-- <optionclicked(option1,option2) -->
                <label class="option" onclick="optionClicked(this.querySelector('span.opt1Target').innerHTML, this.querySelector('span.opt2Target').innerHTML)">                  
                
                <!--input used internall, not sent with form data
                <input type="hidden" value="${match.regex2} -->
                
                <span class="opt1Target">${match.headers[0]}</span><br />
                </label>            
            `)
            .join("");

            if (matchingDataArray.length >4) {
                matchList.style.maxHeight = scrollMax;
                matchList.style.overflowY = "scroll";
            }
            matchList.innerHTML = html;
    }
};

//func 4: MultiSelect Checkbox Logic
const selectTypeLogic = () => {
    if(
        select1.checked ==true || 
        select2.checked == true || 
        selectBoth.checked == true
    ) { 
        selectAny.checked = false;
        selectAny.disabled = true;
    }
}

///////// LISTENERS //////////////
//filter listener
matchList.addEventListener("focusout", () => {
    matchList.style.visibility = "hidden";
})

//filterbox keyup first few letters
filterOpt1.addEventListener("keyup", () => {
    matchList.innerHTML = "";
    filterData(filterOpt1.value)
})

filterOpt2.addEventListener("keyup", () => {
    matchList.innerHTML = "";
    filterData(filterOpt2.value)
})

//listeners to clear: 
opt1.addEventListener("input", () => {
    filterOpt1.innerHTML = ""
    matchList.innerHTML = ""
});
opt2.addEventListener("input", () => {
    filterOpt2.innerHTML = ""
    matchList.innerHTML = ""
})
// MULTI SELECT listener
selectTypes.addEventListener("change", selectTypeLogic);










































