// KosarajuSharirSCC.cpp : Defines the entry point for the console application.
//

#include <string>
#include <vector>
#include <set>
#include <iostream>
#include <unordered_map>
#include <utility>
#include <sstream>
#include <fstream>
#include <chrono>

using namespace std;
using ms = chrono::milliseconds;
using get_time = chrono::steady_clock;

class KosarajuSharirSCC
{
   unordered_map<int, bool> visited;
   unordered_map<int, int> leaderOf;
   int leaderNode = -1;
   vector<int> leaders;
   int finishingTime = 0;
   unordered_map<int, vector<int>> graph;
   unordered_map<int, int> finishingTimeOf;
   unordered_map<int, int> componentSizes;
   int nodes = 0;

public:

   unordered_map<int, vector<int>> reversedGraph;

   KosarajuSharirSCC() = default;

   pair<unordered_map<int, vector<int>>, unordered_map<int, vector<int>>>
   readGraphFromFile(string filename)
   {
      ifstream infile{ filename };
      string line;
      int lastVertex = 0;
      while (std::getline(infile, line))
      {
         istringstream iss{ line };
         int node, edge;
         if (!(iss >> node >> edge)) { break; } // error
         graph[node].push_back(edge);
         reversedGraph[edge].push_back(node);
         lastVertex = node;
      }
      nodes = lastVertex;
      return pair<unordered_map<int, vector<int>>, unordered_map<int, vector<int>>>
            {graph, reversedGraph};
   }

   void __init()
   {
      for (int i = 1; i < nodes + 1; ++i)
      {
         visited[i] = false;
         leaderOf[i] = -1;
         finishingTimeOf[i] = 0;
      }
   }
   
   void __reset()
   {
      for (int i = 1; i < nodes + 1; ++i)
      {
         visited[i] = false;
      }
      leaders = vector<int>{};
      componentSizes = unordered_map<int, int>{};
   }

   void __dsfLoop(unordered_map<int, vector<int>> & graph)
   {
      finishingTime = 0;
      leaderNode = -1;

      for (int i = nodes; i > 0; --i)
      {
         if (!visited[i])
         {
            leaderNode = i;
            leaders.push_back(i);
            __depthFirstSearch(graph, i);
            componentSizes[leaderNode] = 1;
         }
         else
         {
            componentSizes[leaderOf[i]] += 1;
         }
      }
   }

   void __depthFirstSearch(unordered_map<int, vector<int>> & graph, int node)
   {
      visited[node] = true;
      leaderOf[node] = leaderNode;
      for (auto & adjacentNode : graph[node])
      {
         if (!visited[adjacentNode])
         {
            __depthFirstSearch(graph, adjacentNode);
         }
      }
      finishingTime += 1;
      finishingTimeOf[node] = finishingTime;
   }

   unordered_map<int, vector<int>> 
   __createGraphFromFinishingTimes(unordered_map<int, vector<int>> & graph)
   {
      unordered_map<int, vector<int>> result;
      for (int key = 1; key < nodes + 1; ++key)
      {
         for (auto & edge : graph[key])
         {
            result[finishingTimeOf[key]].push_back(finishingTimeOf[edge]);
         }
      }
      return result;
   }

   void findStronglyConnectedComponents(unordered_map<int, vector<int>> & graph)
   {
      __init();
      __dsfLoop(reversedGraph);
      cout << "After\n";
      __reset();
      auto finishingTimesGraph = __createGraphFromFinishingTimes(graph);
      __dsfLoop(finishingTimesGraph);
      //return self.leaders, self.componentSizes;  // each strongly connected component has a single leader
   }
};

int main()
{
   auto sccFinder = KosarajuSharirSCC();
   auto start = get_time::now(); //use auto keyword to minimize typing strokes :)
   auto graphs = sccFinder.readGraphFromFile("SCC.txt");
   auto end = get_time::now();
   auto diff = end - start;
   cout << "Reading of the file take :  " << chrono::duration_cast<ms>(diff).count() << " ms " << endl;
   sccFinder.reversedGraph = graphs.first;

   start = get_time::now(); //use auto keyword to minimize typing strokes :)
   sccFinder.findStronglyConnectedComponents(graphs.first);
   end = get_time::now();
   diff = end - start;
   return 0;
}

