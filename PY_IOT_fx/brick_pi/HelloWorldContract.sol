pragma solidity ^0.4.0;

contract HelloWorldContract {
	string word = "Hellow World";
	address issuer;
	
	function HelloWorldContract(){
		issuer = msg.sender;
	}
	modifier ifIssuer(){
		if(issuer != msg.sender){
			throw;
		}else{
			_;
		}
}
	
	function getWord() constant returns(string) {
		return word;
	}
	function setWord(string newWord) ifIssuer returns(string) { 
		word = newWord;
		return "This is the creator!";
		} 
	}
 