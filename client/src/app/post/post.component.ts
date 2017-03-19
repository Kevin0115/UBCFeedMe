import {Component, OnInit, Input} from '@angular/core';
import {Post} from "../posts/posts.component";

@Component({
  selector: 'app-post',
  templateUrl: './post.component.html',
  styleUrls: ['./post.component.css']
})
export class PostComponent implements OnInit {
  @Input() posts: Array<Post>;

  constructor() { }

  ngOnInit() {
  }

}
