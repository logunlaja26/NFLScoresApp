import { Component, OnInit } from '@angular/core';
import { NflScoresService } from '../nfl-scores.service'

@Component({
  selector: 'app-history',
  templateUrl: './history.component.html',
  styleUrls: ['./history.component.css']
})
export class HistoryComponent implements OnInit {
  characters: Observable<any[]>;
  columns: string[];


  constructor(private atService: NflScoresService) { }

  ngOnInit() {
  	this.columns = this.atService.getColumns();
  	//["Date of Contest","Home team","Away team","Home team scores","Away team scores"]

  	this.characters = this.atService.getCharacters();
  	//all data in mock-data.ts
  }

}
