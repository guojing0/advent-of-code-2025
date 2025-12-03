defmodule DayTwo do
  @moduledoc """
  Finds and sums invalid IDs based on repeated digit patterns.
  """

  def parse_ranges(filename) do
    filename
    |> File.read!()
    |> String.trim()
    |> String.split(",")
    |> Enum.map(&parse_range/1)
  end

  defp parse_range(range) do
    [start, stop] = String.split(range, "-")
    {String.to_integer(start), String.to_integer(stop)}
  end

  def repeated_twice?(n) do
    str = Integer.to_string(n)
    len = String.length(str)
    half = div(len, 2)

    rem(len, 2) == 0 and String.slice(str, 0, half) == String.slice(str, half, half)
  end

  def repeated?(n) do
    str = Integer.to_string(n)
    len = String.length(str)

    len > 1 and
      Enum.any?(1..div(len, 2), &has_repeating_pattern?(str, len, &1))
  end

  defp has_repeating_pattern?(str, len, pattern_len) do
    if rem(len, pattern_len) == 0 do
      pattern = String.slice(str, 0, pattern_len)
      repetitions = div(len, pattern_len)
      String.duplicate(pattern, repetitions) == str
    else
      false
    end
  end

  def find_invalid_ids(ranges, validator) do
    ranges
    |> Enum.flat_map(fn {start, stop} ->
      start..stop |> Enum.filter(validator)
    end)
  end

  def main do
    ranges = parse_ranges("day-two.txt")

    part_one_sum = ranges |> find_invalid_ids(&repeated_twice?/1) |> Enum.sum()
    part_two_sum = ranges |> find_invalid_ids(&repeated?/1) |> Enum.sum()

    IO.puts(part_one_sum)
    IO.puts(part_two_sum)
  end
end

DayTwo.main()
