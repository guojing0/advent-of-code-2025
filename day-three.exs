defmodule DayThree do
  @moduledoc """
  Find the maximum k-digit number by selecting k digits in order from each line.
  """

  def parse_lines(filename) do
    filename
    |> File.read!()
    |> String.trim()
    |> String.split("\n")
  end

  def max_k_digit_number(line, k) do
    # Convert to tuple for O(1) indexing (String.at is O(n)!)
    chars = line |> String.to_charlist() |> List.to_tuple()
    n = tuple_size(chars)

    chars
    |> pick_digits(n, k, 0)
    |> List.to_string()
    |> String.to_integer()
  end

  defp pick_digits(_chars, _n, 0, _cursor), do: []

  defp pick_digits(chars, n, remaining, cursor) do
    # Valid range: [cursor, n - remaining + 1)
    end_pos = n - remaining + 1
    best_pos = find_leftmost_max(chars, cursor, end_pos)

    [elem(chars, best_pos) | pick_digits(chars, n, remaining - 1, best_pos + 1)]
  end

  defp find_leftmost_max(chars, start, end_pos) do
    Enum.reduce((start + 1)..(end_pos - 1)//1, start, fn i, best ->
      if elem(chars, i) > elem(chars, best), do: i, else: best
    end)
  end

  def main do
    lines = parse_lines("day-three.txt")

    part_one = lines |> Enum.map(&max_k_digit_number(&1, 2)) |> Enum.sum()
    part_two = lines |> Enum.map(&max_k_digit_number(&1, 12)) |> Enum.sum()

    IO.puts(part_one)
    IO.puts(part_two)
  end
end

DayThree.main()
