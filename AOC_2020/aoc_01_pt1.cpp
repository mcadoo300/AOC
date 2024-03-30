#include <algorithm> // NOLINT
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

int main() {
  std::ifstream inf{"input_01.txt"};
  if (!inf) {
    std::cerr << "Whoops! File could not be read.\n";
    return 1;
  }
  std::vector<int> nums{};

  std::string strInput{};
  while (inf >> strInput) {
    nums.insert(nums.end(), stoi(strInput));
    // std::cout << stoi(strInput) << '\n';
  }

  std::sort(nums.begin(), nums.end());
  // for (int i =0; i < nums.size();i++)
  //   std::cout << nums[i] << '\n';
  int lower = 0, upper = nums.size() - 1, sum = 0;
  while (sum != 2020) {
    sum = nums[lower] + nums[upper];
    if (sum < 2020) {
      lower++;
    } else if (sum > 2020) {
      upper--;
    }
  }
  std::cout << nums[lower] * nums[upper] << '\n';

  return 0;
}
