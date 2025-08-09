// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract Setup{
    
    bool public solved;
    constructor()payable{
        
    }


    function isSolved()public view returns (bool){
        return solved;
    }


}
