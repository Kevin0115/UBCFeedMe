import { Component, OnInit } from '@angular/core';
import {PostsService} from "../posts.service";

@Component({
  selector: 'app-posts',
  templateUrl: './posts.component.html',
  styleUrls: ['./posts.component.css']
})
export class PostsComponent implements OnInit {
  posts: Array<Post> = [];

  constructor(private postsService: PostsService) { }

  /**
   * Load posts from the server and deserialize the response
   */
  ngOnInit() {
    this.postsService.getAllPosts().subscribe(res => {
      this.posts = res.entries.map(entry => {
        new Post(entry.key1, entry.key2, entry.key3)
      });
    })
  }
}

class Post {
  constructor(
    public val1: string,
    public val2: string,
    public val3: string
  ) { }
}
